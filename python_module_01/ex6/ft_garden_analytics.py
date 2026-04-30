#!/usr/bin/env python3

class Plant:
    class _Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

        def display(self) -> None:
            print(
                f"Stats: {self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = height
        self._age: int = age
        self._stats: Plant._Stats = Plant._Stats()

    def grow(self) -> None:
        self._height += 8.0
        self._stats.grow_calls += 1

    def age_up(self) -> None:
        self._age += 20
        self._stats.age_calls += 1

    def show(self) -> None:
        self._stats.show_calls += 1
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    def display_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._bloomed: bool = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self._shade_calls: int = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self._height, 1)}cm long and "
            f"{self.trunk_diameter}cm wide."
        )

    def display_stats(self) -> None:
        super().display_stats()
        print(f"{self._shade_calls} shade")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age_up(self) -> None:
        super().age_up()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_up()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_plant_stats(unknown)


if __name__ == "__main__":
    main()
