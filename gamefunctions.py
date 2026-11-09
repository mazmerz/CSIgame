# Adventure Functions
# Mazzie Merzanis
# 10/18/26


"""
Provide helper functions for the text-based adventure game.

Includes town actions, combat, healing, shopping, inventory,
equipment, and monsters.
"""

import random

MAX_HEALTH = 30

SHOP_ITEMS = {
    "1": {"name": "health potion", "type": "consumable",
          "price": 25, "healing": 15},
    "2": {"name": "iron sword", "type": "weapon",
          "price": 100, "maxDurability": 10},
    "3": {"name": "shield", "type": "shield",
          "price": 75, "maxDurability": 6},
    "4": {"name": "fire bomb", "type": "special",
          "price": 150, "target": "Dragon"}
}


def print_welcome():
    """Display the welcome message."""
    print("Welcome to the Adventure Game!")
    print("Explore the world, visit the shop, and fight monsters!")


def get_player_name():
    """Ask for a non-empty player name."""
    while True:
        name = input("What is your name, adventurer? ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def get_town_action(state):
    """Display the town menu and return a valid choice."""
    while True:
        print("\n===== Town =====")
        print(f"HP: {state['player_health']} | Gold: {state['player_gold']}")
        print("1) Fight a monster")
        print("2) Sleep")
        print("3) Visit shop")
        print("4) View inventory / Equip items")
        print("5) Quit")

        action = input("Choose an option: ").strip()
        if action in ("1", "2", "3", "4", "5"):
            return action
        print("Invalid choice. Try again.")


def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    """Return the quantity purchased and remaining money."""
    if itemPrice <= 0:
        raise ValueError("Item price must be greater than zero.")
    if startingMoney < 0 or quantityToPurchase < 0:
        raise ValueError("Money and quantity cannot be negative.")

    affordable = startingMoney // itemPrice
    purchased = min(quantityToPurchase, affordable)
    remaining = startingMoney - purchased * itemPrice
    return purchased, remaining


def show_shop(state):
    """Display shop items and allow the player to purchase them."""
    while True:
        print("\n===== Adventure Shop =====")
        print(f"Your gold: {state['player_gold']}")
        print("1. Health Potion - 25 gold")
        print("2. Iron Sword - 100 gold")
        print("3. Shield - 75 gold")
        print("4. Fire Bomb - 150 gold")
        print("5. Leave shop")

        choice = input("Choose an item: ").strip()

        if choice == "5":
            break
        if choice not in SHOP_ITEMS:
            print("Invalid choice.")
            continue

        item_info = SHOP_ITEMS[choice]
        quantity_text = input("How many would you like to buy? ").strip()

        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                print("Enter a positive quantity.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        purchased, remaining = purchase_item(
            item_info["price"], state["player_gold"], quantity
        )

        if purchased == 0:
            print("You don't have enough gold.")
            continue

        state["player_gold"] = remaining

        for _ in range(purchased):
            new_item = item_info.copy()
            if "maxDurability" in new_item:
                new_item["currentDurability"] = new_item["maxDurability"]
            new_item["equipped"] = False
            del new_item["price"]
            state["player_inventory"].append(new_item)

        print(f"You purchased {purchased} {item_info['name']}(s)!")


def show_inventory(state):
    """Display inventory and allow the player to manage items."""
    inventory = state["player_inventory"]

    while True:
        print("\n===== Inventory =====")

        if not inventory:
            print("Your inventory is empty.")
        else:
            for index, item in enumerate(inventory, start=1):
                status = " (Equipped)" if item.get("equipped") else ""
                print(f"{index}. {item['name']}{status}")

                if "currentDurability" in item:
                    print(f"   Durability: {item['currentDurability']}")

        print("\n1. Equip weapon")
        print("2. Equip shield")
        print("3. Use health potion")
        print("4. Return to town")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            equip_item(state, "weapon")
        elif choice == "2":
            equip_item(state, "shield")
        elif choice == "3":
            use_health_potion(state)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def equip_item(state, item_type):
    """Let the player equip an item of the requested type."""
    inventory = state["player_inventory"]
    available = [
        item for item in inventory
        if item["type"] == item_type
        and item.get("currentDurability", 1) > 0
    ]

    equipped_key = "equipped_weapon" if item_type == "weapon" else "equipped_shield"

    if not available:
        print(f"You don't have any usable {item_type}s.")
        return

    print(f"\nChoose a {item_type} to equip:")
    for index, item in enumerate(available, start=1):
        print(f"{index}. {item['name']}")

    print("0. Unequip current item")

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Invalid choice.")
        return

    if choice == 0:
        if state[equipped_key]:
            state[equipped_key]["equipped"] = False
        state[equipped_key] = None
        print(f"Your {item_type} is unequipped.")
    elif 1 <= choice <= len(available):
        if state[equipped_key]:
            state[equipped_key]["equipped"] = False

        selected = available[choice - 1]
        selected["equipped"] = True
        state[equipped_key] = selected
        print(f"You equipped the {selected['name']}!")
    else:
        print("Invalid choice.")


def use_health_potion(state):
    """Use a health potion to restore player health."""
    for item in state["player_inventory"]:
        if item["type"] == "consumable":
            if state["player_health"] >= MAX_HEALTH:
                print("Your health is already full!")
                return

            healing = item["healing"]
            state["player_health"] = min(
                MAX_HEALTH, state["player_health"] + healing
            )
            state["player_inventory"].remove(item)
            print(f"You restored {healing} HP!")
            return

    print("You don't have a health potion.")


def random_monster():
    """Generate a monster with randomized statistics and reward."""
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
        "money": reward
    }


def get_user_fight_action():
    """Ask the player to fight or run away."""
    while True:
        print("\n1) Fight")
        print("2) Run away")
        action = input("Choose an option: ").strip()
        if action in ("1", "2"):
            return action
        print("Invalid choice. Enter 1 or 2.")


def fight_monster(state):
    """Run combat using the player's state dictionary."""
    if state["player_health"] <= 0:
        print("You are too weak to fight. Sleep to restore your HP.")
        return

    monster = random_monster()
    print(f"\nA {monster['name']} appears!")
    print(monster["description"])

    while state["player_health"] > 0 and monster["health"] > 0:
        print(f"\nYour HP: {state['player_health']}")
        print(f"{monster['name']} HP: {monster['health']}")
        print(f"Your gold: {state['player_gold']}")

        action = get_user_fight_action()

        if action == "2":
            print("You ran away!")
            break

        # Give the player a choice to use a fire bomb against a dragon.
        if monster["name"] == "Dragon":
            bombs = [
                item for item in state["player_inventory"]
                if item["type"] == "special"
                and item["target"] == "Dragon"
            ]
            if bombs:
                use_bomb = input(
                    "Use a Fire Bomb to defeat the dragon? (y/n): "
                ).strip().lower()

                if use_bomb == "y":
                    monster["health"] = 0
                    state["player_inventory"].remove(bombs[0])
                    print("The Fire Bomb defeats the dragon instantly!")
                    break

        damage = random.randint(5, 10)
        weapon = state["equipped_weapon"]

        if weapon:
            damage += 5
            weapon["currentDurability"] -= 1
            print("Your sword adds 5 damage!")

            if weapon["currentDurability"] <= 0:
                print("Your sword broke!")
                weapon["equipped"] = False
                state["equipped_weapon"] = None

        monster["health"] -= damage
        print(f"You deal {damage} damage!")

        if monster["health"] > 0:
            damage = random.randint(1, monster["power"])
            shield = state["equipped_shield"]

            if shield:
                damage = max(0, damage - 3)
                shield["currentDurability"] -= 1
                print("Your shield blocks some damage!")

                if shield["currentDurability"] <= 0:
                    print("Your shield broke!")
                    shield["equipped"] = False
                    state["equipped_shield"] = None

            state["player_health"] -= damage
            print(f"The monster deals {damage} damage!")

    if state["player_health"] <= 0:
        state["player_health"] = 0
        print("You passed out! Return to town and sleep.")
    elif monster["health"] <= 0:
        state["player_gold"] += monster["money"]
        print(f"You defeated the {monster['name']}!")
        print(f"You earned {monster['money']} gold!")


def sleep(state):
    """Spend 5 gold to restore the player's health."""
    if state["player_health"] >= MAX_HEALTH:
        print("Your HP is already full!")
    elif state["player_gold"] < 5:
        print("You need at least 5 gold to sleep.")
    else:
        state["player_gold"] -= 5
        state["player_health"] = MAX_HEALTH
        print("You rested and restored your HP!")


if __name__ == "__main__":
    print_welcome()
