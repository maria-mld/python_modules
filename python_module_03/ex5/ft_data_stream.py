import random
from typing import Generator


PLAYERS = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS = ['run', 'eat', 'sleep', 'grab',
           'move', 'swim', 'climb', 'release', 'use']


def get_event() -> Generator[tuple, None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(event_list: list) -> Generator[tuple, None, None]:
    while len(event_list) > 0:
        idx = random.randrange(len(event_list))
        target = event_list.pop(idx)
        yield target


def main():
    print("=== Game Data Stream Processor ===")

    stream = get_event()

    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    event_list = []
    for _ in range(10):
        event_list.append(next(stream))

    print(f"\nBuilt list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
