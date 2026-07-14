from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells and call both with the same arguments."""
    def combined(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a spell that casts the base spell with multiplied power."""
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that runs only when its condition is true."""
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts every spell in sequence."""
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    """Cast a damage spell at the target."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Cast a healing spell on the target."""
    return f"Heals {target} for {power} HP"


def main() -> None:
    """Run examples for the higher-order spell functions."""
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    dmg, hp = combined("Dragon", 20)
    print(
        f"Combined spell result: {dmg.split(' for ')[0]}, "
        f"{hp.split(' for ')[0]}"
    )

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    safe_fireball = conditional_caster(lambda target, power: power >= 15,
                                       fireball)
    print(safe_fireball("Dragon", 20))
    print(safe_fireball("Dragon", 5))

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal, fireball])
    for result in combo("Dragon", 10):
        print(result)

    print("\ncallable(fireball):", callable(fireball))
    print("callable('not a function'):", callable("not a function"))


if __name__ == "__main__":
    main()
