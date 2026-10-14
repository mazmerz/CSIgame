# Adventure Functions
# Mazzie Merzanis
# 10/2/26

import random

def purchase_item(itemPrice, startingMoney, quantityToPurchase=1):
    # Determine the maximum number of items the player can afford
    maximumAffordable = startingMoney // itemPrice

    # The player cannot buy more than they requested
    quantityPurchased = min(quantityToPurchase, maximumAffordable)

    # Calculate the money left after the purchase
    moneyRemaining = startingMoney - (quantityPurchased * itemPrice)

    return quantityPurchased, moneyRemaining
def new_random_monster():
    # Randomly choose one of three monster types
    monsterType = random.randint(1, 3)

    if monsterType == 1:
        monsterName = "A goblin"
        monsterDescription = "This is a lone goblin. When it notices you, it rushes at you quickly with a sharp dagger drawn."
        monsterHealth = random.randint(5, 10)
        monsterPower = random.randint(2, 5)
        monsterMoney = random.randint(10, 50)

    elif monsterType == 2:
        monsterName = "An orc"
        monsterDescription = "A large orc blocks your path. It carries a heavy axe and looks ready for a fight."
        monsterHealth = random.randint(15, 25)
        monsterPower = random.randint(6, 10)
        monsterMoney = random.randint(50, 150)

    else:
        monsterName = "A dragon"
        monsterDescription = "A massive dragon watches you carefully. Smoke rises from its nostrils as it prepares to attack."
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


# Test purchase_item() three times

purchased, moneyLeft = purchase_item(123, 1000, 3)
print("Purchase Test 1:")
print("Items purchased:", purchased)
print("Money remaining:", moneyLeft)

purchased, moneyLeft = purchase_item(123, 201, 3)
print("\nPurchase Test 2:")
print("Items purchased:", purchased)
print("Money remaining:", moneyLeft)

purchased, moneyLeft = purchase_item(341, 2112)
print("\nPurchase Test 3:")
print("Items purchased:", purchased)
print("Money remaining:", moneyLeft)


# Test new_random_monster() three times

monster1 = new_random_monster()
print("\nMonster Test 1:")
print(monster1)

monster2 = new_random_monster()
print("\nMonster Test 2:")
print(monster2)

monster3 = new_random_monster()
print("\nMonster Test 3:")
print(monster3)
