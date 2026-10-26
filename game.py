
"""
Run the main adventure game.

The main loop lets the player fight monsters, sleep, or quit.
"""

import gamefunctions


def main():
    """Run the main game loop."""
    player_name = gamefunctions.get_player_name()
    health = 30
    gold = 10

    gamefunctions.print_welcome()
    print(f"\nWelcome, {player_name}!")

    while True:
        action = gamefunctions.get_town_action(health, gold)
        if action == "1":
            health, gold = gamefunctions.fight_monster(health, gold)
        elif action == "2":
            health, gold = gamefunctions.sleep(health, gold)
        elif action == "3":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
