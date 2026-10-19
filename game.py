"""
Run the main adventure game.

This program imports gamefunctions to display the welcome
message and shop, process a purchase, and generate a monster.
"""

import gamefunctions


def main():
    """
    Run the adventure game and interact with the player.

    Parameters:
        None

    Returns:
        None
    """
    playerName = input("What is your name, adventurer? ")

    print()
    gamefunctions.print_welcome()
    print(f"\nWelcome, {playerName}!")

    # Display the shop menu.
    gamefunctions.print_shop_menu()

    # Let the player attempt to purchase a health potion.
    startingMoney = 100
    itemPrice = 25

    print(f"\nYou have ${startingMoney}.")
    quantity = int(input("How many health potions would you like? "))

    try:
        purchased, moneyLeft = gamefunctions.purchase_item(
            itemPrice, startingMoney, quantity
        )

        print(f"You purchased {purchased} health potion(s).")
        print(f"Money remaining: ${moneyLeft}")

    except ValueError as error:
        print("Purchase error:", error)
        return

    # Generate a random monster.
    monster = gamefunctions.random_monster()

    print("\nA monster appears!")
    print(monster["description"])
    print("Monster:", monster["name"])
    print("Health:", monster["health"])
    print("Power:", monster["power"])
    print("Money reward:", monster["money"])


if __name__ == "__main__":
    main()
