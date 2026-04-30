#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = 0.0
        self.age: int = 0

        if height < 0:
            print("f{self.name}: Error, height can't be negative")
        else:
            self.height = height

        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self.age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self.height = height
        print(f"Height updated: {int(height)}cm")

    def get_height(self) -> float:
        return self.height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self.age = age
        print(f"Age updated: {age} days\n")

    def get_age(self) -> int:
        return self.age

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old\n")


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    plant.show()

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-10)

    print("Current state:", end=" ")
    plant.show()


if __name__ == "__main__":
    main()
