def create_inventory(items: list[str]) -> dict[str, int]:
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory: dict[str, int]):
    result = []
    for item, count in inventory.items():
        if count > 0:
            result.append((item, count))
    return result