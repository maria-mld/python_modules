from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1 import HealCapability, TransformCapability
from ex0 import Creature


def test_healing() -> None:
    print("Testing Creature with healling capability")
    factory = HealingCreatureFactory()

    print("base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    if isinstance(base, HealCapability):
        print(base.heal())

    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    def run_sequence(creature: Creature) -> None:
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
    
    print("base:")
    run_sequence(factory.create_base())

    print("evolved:")
    run_sequence(factory.create_evolved())


def main() -> None:
    test_healing()
    test_transform()


if __name__ == "__main__":
    main()
