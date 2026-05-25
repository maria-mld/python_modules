from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name: str = name
        self.creature_type: str = creature_type

    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__(name="Flameling", creature_type="Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Pyrodon", creature_type="Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__(name="Aquabub", creature_type="Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__(name="Torragon", creature_type="Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
