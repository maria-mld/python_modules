#!/usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        groth_rate: float
    ) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age
        self.groth_rate: float = groth_rate

    def grow(self) -> None:
        self.height += self.groth_rate

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def main() -> None:
    plant = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Groth ===")
    plant.show()

    initial_height: float = plant.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.age_up()
        plant.show()

    total_groth: float = plant.height - initial_height
    print(f"Groth this week: {round(total_groth, 1)}cm")


if __name__ == "__main__":
    main()
