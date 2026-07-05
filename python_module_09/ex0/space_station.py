from pydantic import BaseModel, Field, ValidationError
from datetime import datetime, date


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=0, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)

    def __str__(self) -> str:
        status: str = ('Operational' if self.is_operational
                       else 'Non operational')
        return (
            f"ID: {self.station_id}\n"
            f"Name: {self.name}\n"
            f"Crew: {self.crew_size}\n"
            f"Power: {self.power_level}\n"
            f"Oxygen: {self.oxygen_level}\n"
            f"Status: {status}"
        )


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    print("Valid station created:")

    try:
        valid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=date.today(),
            is_operational=True
        )
        print(valid_station)
    except ValidationError as e:
        print(f"Error: {e}")
    try:
        print("\n\n========================================")
        print("Expected validation error:")
        valid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=22,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=date.today(),
            is_operational=True
        )
        print(valid_station)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
