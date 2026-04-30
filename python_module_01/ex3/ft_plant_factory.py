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
        self.height += self.growth_rate

    def age_up(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")


def main() -> None:
    plants = [
        Plant("Rose", 25.0, 30, 0.8),
        Plant("Oak", 200.0, 365, 0.3),
        Plant("Cactus", 5.0, 90, 0.1),
        Plant("Sunflower", 80.0, 45, 1.2),
        Plant("Fern", 15.0, 120, 0.5),
    ]

    print("=== Plant Factory Output ===")

    for plant in plants:
        print("Created:", end=" ")
        plant.show()


if __name__ == "__main__":
    main()
