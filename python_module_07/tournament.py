from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def run_tournament(
    tournament_name: str, 
    opponents: List[Tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print(f"{tournament_name}")
    names = []
    for f, s in opponents:
        f_name = f.__class__.__name__.replace("Factory", "").replace("Creature", "")
        s_name = s.__class__.__name__.replace("Strategy", "")
        names.append(f"({f_name}+{s_name})")
    print(f"[ {', '.join(names)} ]")
    
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    fighters = [(fac.create_base(), strat) for fac, strat in opponents]

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            c1, s1 = fighters[i]
            c2, s2 = fighters[j]

            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")

            try:
                actions1 = s1.act(c1)
                actions2 = s2.act(c2)
                print(actions1)
                print(actions2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return

def main() -> None:
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    trans_f = TransformCreatureFactory()

    normal_s = NormalStrategy()
    aggressive_s = AggressiveStrategy()
    defensive_s = DefensiveStrategy()

    # Турнир 0 (Базовый)
    t0_opponents = [
        (flame_f, normal_s),
        (heal_f, defensive_s)
    ]
    run_tournament("Tournament 0 (basic)", t0_opponents)
    print()

    # Турнир 1 (С ошибкой)
    t1_opponents = [
        (flame_f, aggressive_s),  # Ошибка! Flameling не умеет трансформироваться
        (heal_f, defensive_s)
    ]
    run_tournament("Tournament 1 (error)", t1_opponents)
    print()

    # Турнир 2 (Множественный)
    t2_opponents = [
        (aqua_f, normal_s),
        (heal_f, defensive_s),
        (trans_f, aggressive_s)
    ]
    run_tournament("Tournament 2 (multiple)", t2_opponents)


if __name__ == "__main__":
    main()
