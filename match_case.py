# Match cases van characters.
player_class = "Mage"

match player_class:
    case "Warrior":
        health = 150
        damage = 20
        print(f"Class: {player_class}, health: {health}, damage: {damage}")
    case "Mage":
        health = 80
        damage = 35
        print(f"Class: {player_class}, health: {health}, damage: {damage}")
    case "Archer":
        health = 100
        damage = 25
        print(f"Class: {player_class}, health: {health}, damage: {damage}")
    case "Rogue":
        health = 90
        damage = 30
        print(f"Class: {player_class}, health: {health}, damage: {damage}")
    case "Paladin":
        health = 95
        damage = 40
        print(f"Class: {player_class}, health: {health}, damage: {damage}")
    case "Healer":
        health = 110
        damage = 10
        print(f"Class: {player_class}, health: {health}, damage: {damage}")
    case _:
        print("Onbekende class gekozen!")