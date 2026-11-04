# Boodschappenlijst aanmaken.=
boodschappen_lijst = ["Pasta","Tomatensaus","Geraspte kaas","Kruiden","Kip"]

# Nieuwe producten aan boodschappenlijst toevoegen.
boodschappen_lijst.append("Kokosmelk")
boodschappen_lijst.append("Boter")

# Één product verwijderen uit de boodschappenlijst.
boodschappen_lijst.remove("Geraspte kaas")

# Aantal producten in de boodschappenlijst tonen.
len(boodschappen_lijst)
print(len(boodschappen_lijst))
print(boodschappen_lijst)

# Controleer of een bepaald product in de boodschappen list staat.
print("Kip" in boodschappen_lijst)
print("Melk" in boodschappen_lijst)