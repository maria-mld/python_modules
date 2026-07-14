from collections.abc import Callable
import functools
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce a list of spell power values into a single value
    using functools.reduce and the operator module.
    """
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """
    Create three specialized enchantment casters using functools.partial,
    each pre-filled with power=50 and a specific element.
    """
    fire_cast = functools.partial(base_enchantment, power=50, element="Fire")
    ice_cast = functools.partial(base_enchantment, power=50, element="Ice")
    lightning_cast = functools.partial(base_enchantment, power=50,
                                       element="Lightning")

    return {
        "fire": fire_cast,
        "ice": ice_cast,
        "lightning": lightning_cast,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number, memoized with lru_cache
    to avoid recomputation of already-seen values.
    """
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """
    Create a singledispatch-based spell casting system that behaves
    differently depending on the type of the argument it receives.
    """

    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def base_enchantment(power: int, element: str, target: str) -> str:
    """Example enchantment function used to demonstrate partial_enchanter."""
    return f"{element} enchantment ({power} power) cast on {target}"


def main() -> None:
    """Run examples for the functools-based helper functions."""
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")
    print(f"Empty list: {spell_reducer([], 'add')}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    print(enchanters["fire"](target="Dragon"))
    print(enchanters["ice"](target="Golem"))
    print(enchanters["lightning"](target="Wraith"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast([1, 2, 3]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
