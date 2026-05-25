from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    pass

class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True
    
    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this normal strategy"
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    """Агрессивная стратегия: только для трансформеров."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this aggressive strategy"
            )
        # Так как mypy должен быть уверен, что методы существуют,
        # делаем явное приведение/проверку, хотя мы уже проверили в is_valid
        assert isinstance(creature, TransformCapability)
        
        t_start = creature.transform()
        attack = creature.attack()
        t_end = creature.revert()
        return f"{t_start}\n{attack}\n{t_end}"


class DefensiveStrategy(BattleStrategy):
    """Защитная стратегия: только для целителей."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' for this defensive strategy"
            )
        assert isinstance(creature, HealCapability)
        
        attack = creature.attack()
        heal = creature.heal()
        return f"{attack}\n{heal}"
