import random


def main():
    print("=== Game Data Alchemist ===")

    initial_players = ['Alice', 'bob', 'Charlie', 'dylan',
                       'Emma', 'Gregory', 'john', 'kevin', 'Vlad', 'Alibi']
    print(f"Initial list of players: {initial_players}")

    all_cap = [name.capitalize() for name in initial_players]
    print(f"New list with all names capitalized: {all_cap}")

    only_cap = [name for name in initial_players if name.istitle()]
    print(f"New list of capitalized names only: {only_cap}")

    scores = {name: random.randint(1, 1000) for name in all_cap}
    print(f"Score dict: {scores}")

    avg = sum(scores.values()) / len(scores)
    print(f"Score average is {round(avg, 2)}")

    high_scores = {name: score for name,
                   score in scores.items() if score > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
