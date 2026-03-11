"""
Хранилище представляет собой ассоциативный массив вида { "позиция": остаток }, например { "wood": 7, "diamond": 0 }.

Разработайте набор функций для управления хранилищем:

1. Создание хранилища
2. Добавление товаров (приёмка)
3. Уменьшение количества товаров (отгрузка)
4. Удаление позиции
5. Выгрузка товаров с ненулевым остатком
"""


def create_inventory(items: list[str]) -> dict[str, int]:
    """Формирует словарь для отслеживания остатков по каждой из позиций.

    >>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
    {'coal': 1, 'wood': 2, 'diamond': 3}

    :param items: list[str] - исходный список товаров.
    :return: dict[str, int] - словарь с информацией об остатках.
    """
    inventory = {}

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Добавляет новые позиции либо увеличивает количество остатка
    по существующим позициям на основе списка.

    >>> add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
    {'coal': 2, 'wood': 2, 'iron': 1}

    :param inventory: dict[str, int] - текущая версия хранилища.
    :param items: list[str] - приход новых товаров.
    :return: dict[str, int] - обновленное хранилище.
    """
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory



def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Уменьшает количество остатков на основании заказа на отгрузку.

    >>> decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
    {'coal': 2, 'diamond': 0, 'iron': 3}

    Если запрос на конкретную позицию превышает имеющееся количество,
    например, при наличии 3 единиц дерева требуется отгрузить 5,
    отгружает все имеющиеся, оставляя в остатке 0, а оставшиеся две единицы игнорируются.

    >>> decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
    {'coal': 0, 'wood': 0, 'diamond': 1}

    :param inventory: dict[str, int] - текущая версия хранилища.
    :param items: list[str] - список товаров на отгрузку (заказ).
    :return: dict[str, int] - обновленное хранилище.
    """
    for item in items:
        if item in inventory:
           if inventory[item] > 0:
               inventory[item] -= 1

    return inventory



def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    """Удаляет позицию из хранилища.

    >>> remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
    {'wood': 1, 'diamond': 2}

    Если позиция не представлена в хранилище, необходимо вернуть исходную версию хранилища.

    >>> remove_item({"coal":2, "wood":1, "diamond":2}, "gold")
    {'coal': 2, 'wood': 1, 'diamond': 2}

    :param inventory: dict[str, int] - текущая версия хранилища.
    :param item: str - именование позиции для удаления.
    :return: dict[str, int] - обновленное хранилище (исходное, если позиция не найдена).
    """
    if item in inventory:
        del inventory[item]

    return inventory



def list_inventory(inventory: dict[str, int]):
    """Выгружает информацию по позициям с ненулевым остатком.

    >>> list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
    [('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]

    :param inventory: dict[str, int] - хранилище.
    :return: list[tuple[str, int]] - кортежи (позиция, количество) для позиций, по которым имеются остатки.
    """
    result = []

    for item in inventory:
        if inventory[item] > 0:
            result.append((item, inventory[item]))

    result.sort()

    return result
