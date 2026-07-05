from pydantic import BaseModel, Field, model_validator, ValidationError
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepatic = "telepatic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_alien_contact(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')
        if self.contact_type == ContactType.telepatic and self.witness_count < 3:
            raise ValueError('Telepathic contact requires at least 3 witnesses')
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError('Strong signals (> 7.0) should include received messages')
        return self
    
    def __str__(self) -> str:
        return (
            f"ID: {self.contact_id}\n"
            f"Type: {self.contact_type}\n"
            f"Location: {self.location}\n"
            f"Signal: {self.signal_strength}\n"
            f"Duration: {self.duration_minutes}\n"
            f"Witnesses: {self.witness_count}\n"
            f"Message: {self.message_received}"
        )

def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        valid_data = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(valid_data)
    except ValidationError as e:
        print(e)
    print("======================================")

    try:
        AlienContact(
            contact_id="AC_dlfkjsdlfks",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()

