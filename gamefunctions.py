# Adventure Functions
# Mazzie Merzanis
# 10/18/26

"""
Provide helper functions for a text-based adventure game.

This module contains functions for welcoming the player, displaying
the shop menu, purchasing items, and generating random monsters.

The random module is used to generate monster statistics.
Import this module into game.py to use its functions.
"""

import random


def print_welcome():
    """
    Welcome the player to the adventure game.

    Parameters:
        None

    Returns:
        None
    """
    print("Welcome to the Adventure Game!")
    print("Explore the world, visit the shop, and fight monsters!")


def print_shop_menu():
    """
    Display the items available for purchase in the shop.

    Parameters:
        None

    Returns:
        None
    """
    print("\n===== Adventure Shop =====")
    print("1. Health Potion - $25")
    print("2. Iron Sword - $100")
    print("3. Shield - $75")
    print("==========================")


def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """
    Calculate how many items a player can afford.

    Parameters:
        itemPrice (int): The price of one item.
        startingMoney (int): The player's available money.
        quantityToPurchase (int): The requested quantity. Defaults to 1.

    Returns:
        tuple: The quantity purchased and money remaining.
    """
    if itemPrice <= 0:
        raise ValueError("Item price must be greater than zero.")

    if startingMoney < 0 or quantityToPurchase < 0:
        raise ValueError("Money and quantity cannot be negative.")

    maximumAffordable = startingMoney // itemPrice
    quantityPurchased = min(quantityToPurchase, maximumAffordable)
    moneyRemaining = startingMoney - (quantityPurchased * itemPrice)

    return quantityPurchased, moneyRemaining


def random_monster():
    """
    Generate a random monster with its statistics and reward.

    Parameters:
        None

    Returns:
        dict: Monster name, description, health, power, and money reward.
    """
    monsterType = random.randint(1, 3)

    if monsterType == 1:
        monsterName = "A goblin"
        monsterDescription = (
            "A goblin rushes toward you with a sharp dagger."
        )
        monsterHealth = random.randint(5, 10)
        monsterPower = random.randint(2, 5)
        monsterMoney = random.randint(10, 50)

    elif monsterType == 2:
        monsterName = "An orc"
        monsterDescription = (
            "A large orc blocks your path with a heavy axe."
        )
        monsterHealth = random.randint(15, 25)
        monsterPower = random.randint(6, 10)
        monsterMoney = random.randint(50, 150)

    else:
        monsterName = "A dragon"
        monsterDescription = (
            "A massive dragon watches you as smoke rises "
            "from its nostrils."
        )
        monsterHealth = random.randint(40, 60)
        monsterPower = random.randint(12, 20)
        monsterMoney = random.randint(200, 500)

    monster = {
        "name": monsterName,
        "description": monsterDescription,
        "health": monsterHealth,
        "power": monsterPower,
        "money": monsterMoney
    }

    return monster


def test_functions():
    """
    Test each of the four game functions.

    Parameters:
        None

    Returns:
        None
    """
    print_welcome()
    print_shop_menu()

    print("\nPurchase Test 1:")
    purchased, moneyLeft = purchase_item(123, 1000, 3)
    print("Items purchased:", purchased)
    print("Money remaining:", moneyLeft)

    print("\nPurchase Test 2:")
    purchased, moneyLeft = purchase_item(123, 201, 3)
    print("Items purchased:", purchased)
    print("Money remaining:", moneyLeft)

    print("\nPurchase Test 3:")
    purchased, moneyLeft = purchase_item(341, 2112)
    print("Items purchased:", purchased)
    print("Money remaining:", moneyLeft)

    print("\nRandom Monster Tests:")
    for number in range(1, 4):
        monster = random_monster()
        print(f"Monster Test {number}:")
        print(monster)


if __name__ == "__main__":
    test_functions()
