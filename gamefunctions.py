# Adventure Functions
# Mazzie Merzanis
# 10/18/26

"""
Provide helper functions for the text-based adventure game.

Includes town actions, combat, healing, purchases, and monsters.
"""

import random


MAX_HEALTH = 30


def print_welcome():
    """Display the welcome message."""
    print("Welcome to the Adventure Game!")
    print("Explore the world, visit the shop, and fight monsters!")


def print_shop_menu():
    """Display the shop menu."""
    print("\n===== Adventure Shop =====")
    print("1. Health Potion - $25")
    print("2. Iron Sword - $100")
    print("3. Shield - $75")
    print("==========================")


def get_player_name():
    """Ask for a non-empty player name."""
    while True:
        name = input("What is your name, adventurer? ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def get_town_action(health, gold):
    """Display the town menu and return a valid choice."""
    while True:
        print("\nYou are in town.")
        print(f"Current HP: {health}, Current Gold: {gold}")
        print("What would you like to do?")
        print("1) Leave town (Fight Monster)")
        print("2) Sleep (Restore HP for 5 Gold)")
        print("3) Quit")

        action = input("Choose an option: ").strip()
        if action in ("1", "2", "3"):
            return action
        print("Invalid choice. Please enter 1, 2, or 3.")


def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """Return the quantity purchased and the remaining money."""
    if itemPrice <= 0:
        raise ValueError("Item price must be greater than zero.")
    if startingMoney < 0 or quantityToPurchase < 0:
        raise ValueError("Money and quantity cannot be negative.")

    affordable = startingMoney // itemPrice
    purchased = min(quantityToPurchase, affordable)
    remaining = startingMoney - purchased * itemPrice
    return purchased, remaining


def random_monster():
    """Generate a monster with randomized statistics and a reward."""
    monster_type = random.randint(1, 3)

    if monster_type == 1:
        name = "Goblin"
        description = "A goblin rushes toward you with a sharp dagger."
        health = random.randint(5, 10)
        power = random.randint(2, 5)
        reward = random.randint(10, 50)
    elif monster_type == 2:
        name = "Orc"
        description = "A large orc blocks your path with a heavy axe."
        health = random.randint(15, 25)
        power = random.randint(6, 10)
        reward = random.randint(50, 150)
    else:
        name = "Dragon"
        description = "A massive dragon breathes smoke from its nostrils."
        health = random.randint(40, 60)
        power = random.randint(12, 20)
        reward = random.randint(200, 500)

    return {
        "name": name,
        "description": description,
        "health": health,
        "power": power,
        "money": reward,
    }


def get_user_fight_action():
    """Ask the player to fight or run away."""
    while True:
        print("\n1) Fight")
        print("2) Run away")
        action = input("Choose an option: ").strip()
        if action in ("1", "2"):
            return action
        print("Invalid choice. Please enter 1 or 2.")


def display_fight_statistics(health, gold, monster):
    """Display the current player and monster statistics."""
    print(f"\nYour HP: {health} | Gold: {gold}")
    print(f"{monster['name']} HP: {monster['health']}")


def fight_monster(health, gold):
    """Run a combat encounter and return the updated health and gold."""
    if health <= 0:
        print("You are too weak to fight. Sleep to restore your HP.")
        return health, gold

    monster = random_monster()
    print(f"\nA {monster['name']} appears!")
    print(monster["description"])

    while health > 0 and monster["health"] > 0:
        display_fight_statistics(health, gold, monster)
        action = get_user_fight_action()
        if action == "2":
            print("You ran away!")
            break

        damage = random.randint(5, 10)
        monster["health"] -= damage
        print(f"You deal {damage} damage!")

        if monster["health"] > 0:
            damage = random.randint(1, monster["power"])
            health -= damage
            print(f"The monster deals {damage} damage!")

    if health <= 0:
        health = 0
        print("You passed out! Return to town and sleep.")
    elif monster["health"] <= 0:
        gold += monster["money"]
        print(f"You defeated the {monster['name']}!")
        print(f"You earned {monster['money']} gold!")

    return health, gold


def sleep(health, gold):
    """Spend 5 gold to restore the player's health."""
    if health >= MAX_HEALTH:
        print("Your HP is already full!")
    elif gold < 5:
        print("You need at least 5 gold to sleep.")
    else:
        gold -= 5
        health = MAX_HEALTH
        print("You rested and restored your HP!")
    return health, gold


def test_functions():
    """Run basic tests of the helper functions."""
    print_welcome()
    print_shop_menu()
    print("\nPurchase test:", purchase_item(25, 100, 3))
    print("\nRandom monster test:", random_monster())


if __name__ == "__main__":
    test_functions()
