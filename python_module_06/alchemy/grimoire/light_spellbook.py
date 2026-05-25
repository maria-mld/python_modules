def light_spell_allowed_ingridients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    status = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({status})"
