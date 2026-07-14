import time
import random
from collections.abc import Callable
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    """Measure and print the execution time of a spell."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Create a decorator that enforces a minimum spell power."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power")
            if power is None and len(args) >= 2:
                power = args[-1]
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Create a decorator that retries a failed spell cast."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... (attempt {attempt}/"
                              f"{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """Provide mage-related validation and spell-casting behavior."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check that a mage name has at least three alphabetic characters."""
        return len(name) >= 3 and all(char.isalpha() or char.isspace()
                                      for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell when the supplied power passes validation."""
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Cast a fireball after a brief simulated delay."""
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    """Always fail to demonstrate the retry decorator."""
    raise RuntimeError("Spell fizzled unexpectedly")


@retry_spell(max_attempts=3)
def lucky_spell() -> str:
    """Succeed randomly to demonstrate retry behavior."""
    if random.random() < 0.7:
        raise RuntimeError("Spell fizzled")
    return "Waaaaaaagh spelled !"


def main() -> None:
    """Run examples for the spell-related decorators."""
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")
    print(unstable_spell())

    print("\nTesting lucky spell...")
    print(lucky_spell())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("A1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
