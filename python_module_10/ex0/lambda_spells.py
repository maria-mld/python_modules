from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sorting by power in descending order."""
    return sorted(
        artifacts,
        key=lambda artifact: artifact['power'],
        reverse=True,
    )


def power_filter(
    mages: list[dict[str, Any]], min_power: int
) -> list[dict[str, Any]]:
    """Return mages whose power meets the minimum threshold."""
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(
    spells: list[str],
) -> list[str]:
    """Decorate each spell name for display."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float]:
    """Calculate maximum, minimum, and average mage power."""
    powers = list(map(lambda mage: mage['power'], mages))
    return {
        'max_power': max(powers, key=lambda power: power),
        'min_power': min(powers, key=lambda power: power),
        'avg_power': round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    """Run examples for the lambda-based helper functions."""
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'sword'},
    ]

    mages = [
        {'name': 'Merlin', 'power': 95, 'element': 'arcane'},
        {'name': 'Ignis', 'power': 60, 'element': 'fire'},
        {'name': 'Aqua', 'power': 40, 'element': 'water'},
    ]

    spells = ['fireball', 'heal', 'shield']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) comes before "
          f"{second['name']} ({second['power']} power)")

    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 50)
    print([mage['name'] for mage in strong_mages])

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(' '.join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    main()
