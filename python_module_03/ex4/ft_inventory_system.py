import sys


def main():
    print("=== Inventory System Analysis ===")

    inventory = {}

    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name = parts[0]
        qty_str = parts[1]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            qty = int(qty_str)
            inventory[item_name] = qty
        except ValueError as e:
            print(f"Quantity error for {item_name}: {e}")
            continue

    if len(inventory) == 0:
        inventory.update({'magic_item': 1})
        print(f"\nUpdated inventory: {inventory}")
        return

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    if total_qty > 0:
        for item, qty in inventory.items():
            percentage = round((qty / total_qty) * 100, 1)
            print(f"Item {item} represents {percentage}%")

    first_item = item_list[0]
    most_item = first_item
    least_item = first_item
    most_qty = inventory[first_item]
    least_qty = inventory[first_item]

    for item, qty in inventory.items():
        if qty > most_qty:
            most_qty = qty
            most_item = item
        if qty < least_qty:
            least_qty = qty
            least_item = item

    print(f"Item most abudant: {most_item} with quantity {most_qty}")
    print(f"Item least abudant: {least_item} with quantity {least_qty}")

    inventory.update({'magic_item': 1})
    print(f"\nUpdated inventory: {inventory}")


if __name__ == "__main__":
    main()
