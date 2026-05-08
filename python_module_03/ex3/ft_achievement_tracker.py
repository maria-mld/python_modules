import random


MASTER_ACHIEVEMENTS = [
    'Crafting Genius', 'Strategist', 'World Savior', 'Master Explorer',
    'Collector Supreme', 'Untouchable', 'Boss Slayer', 'Unstoppable',
    'Speed Runner', 'Survivor', 'Treasure Hunter', 'First Steps',
    'Sharp Mind', 'Hidden Path Finder'
]


def gen_player_achievements():
    num_achievements = random.randint(6, 9)
    chosen = random.sample(MASTER_ACHIEVEMENTS, num_achievements)
    return set(chosen)


def main():
    print("=== Achievement Tracker System ===\n")
    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print()

    all_distinct = set()
    for achievements in players.values():
        all_distinct = all_distinct.union(achievements)
    print(f"\nAll distinct achievements: {all_distinct}")

    common = set(MASTER_ACHIEVEMENTS)
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"\nCommon achievements: {common}")

    for name, achievements in players.items():
        others_achievements = set()

        for other_name, other_achievements in players.items():
            if name != other_name:
                others_achievements = others_achievements.union(
                    other_achievements)

        exclusive = achievements.difference(others_achievements)
        print(f"Only {name} has: {exclusive}")

    master_set = set(MASTER_ACHIEVEMENTS)
    for name, achievements in players.items():

        missing = master_set.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
