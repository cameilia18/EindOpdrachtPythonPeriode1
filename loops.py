# Monster variabele maken.
monster = [100, 150, 200]
player_damage = 25

# For-while loop voor de health van de monster en aantal aanvalling.
for monster_health in monster:
    aantal_aanvallen = 0

    while monster_health > 0:
      monster_health = monster_health - player_damage
      aantal_aanvallen = aantal_aanvallen + 1
      print(f"Monster heeft nu {monster_health} health.")

    print (f"Het monster is verslagen na {aantal_aanvallen} aanvallen.")

