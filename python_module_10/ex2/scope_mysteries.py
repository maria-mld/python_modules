from collections.abc import Callable


def mage_counter() -> Callable:
    """Create an independent counter for mage-related events."""
    count = 0

    def counter() -> int:
        """Increment and return the captured counter value."""
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Create an accumulator initialized with the given power."""
    total = initial_power

    def accumulate(amount: int) -> int:
        """Add an amount to and return the captured total."""
        nonlocal total
        total += amount
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    """Create an enchantment function for the specified type."""
    def enchant(item_name: str) -> str:
        """Apply the captured enchantment type to an item name."""
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    """Create paired functions for storing and recalling values."""
    storage: dict = {}

    def store(key: str, value) -> None:
        """Store a value under a key in the captured vault."""
        storage[key] = value

    def recall(key: str):
        """Return the value for a key or a default message."""
        return storage.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main() -> None:
    """Run examples that demonstrate closures and captured state."""
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    flame_enchant = enchantment_factory("Flaming")
    frost_enchant = enchantment_factory("Frozen")
    print(flame_enchant("Sword"))
    print(frost_enchant("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
