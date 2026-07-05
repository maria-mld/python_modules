from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_safety(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        if not any(m.rank in
                   (Rank.COMMANDER, Rank.CAPTAIN) for m in self.crew):
            raise ValueError("Need at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced < len(self.crew) / 2:
                raise ValueError("Long mission needs 50% experienced crew")

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew must be active")

        return self


def main():
    print("Space Mission Crew Validation\n" + "=" * 40)

    print("Valid mission:")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 1),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="CR001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=42,
                    specialization="Mission Command",
                    years_experience=15,
                ),
                CrewMember(
                    member_id="CR002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=8,
                ),
                CrewMember(
                    member_id="CR003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=29,
                    specialization="Engineering",
                    years_experience=3,
                ),
            ],
        )

        print("Mission:", mission.mission_name)
        print("ID:", mission.mission_id)
        print("Destination:", mission.destination)
        print("Duration:", mission.duration_days)
        print("Budget:", mission.budget_millions)
        print("Crew size:", len(mission.crew))

    except ValidationError as error:
        for e in error.errors():
            print(e["msg"].replace("Value error, ", ""))

    print("\n" + "=" * 40)

    print("Invalid mission:")
    try:
        mission = SpaceMission(
            mission_id="M2024_LUNA",
            mission_name="Lunar Survey Run",
            destination="Moon",
            launch_date=datetime(2024, 9, 15),
            duration_days=30,
            budget_millions=50.0,
            crew=[
                CrewMember(
                    member_id="CR010",
                    name="Bob Lee",
                    rank=Rank.LIEUTENANT,
                    age=31,
                    specialization="Navigation",
                    years_experience=6,
                ),
                CrewMember(
                    member_id="CR011",
                    name="Mia Chen",
                    rank=Rank.OFFICER,
                    age=27,
                    specialization="Engineering",
                    years_experience=2,
                ),
            ],
        )

        print("Mission:", mission.mission_name)

    except ValidationError as error:
        for e in error.errors():
            print(e["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
