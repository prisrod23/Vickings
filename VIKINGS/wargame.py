
from vikingsClasses import Soldier, Viking, Saxon, War
import random

soldier_names = ["Aran", "Arnau", "Papi", "Kyara", "Mami", "Lala", "Lalo", "Tito", "Claudia", "Avi", "Avia"]

# Crear una instancia de la guerra
war = War()

# Crear 5 Vikings y agregarlos a la guerra
for _ in range(5):
    viking = Viking(soldier_names[random.randint(0, 10)], 100, random.randint(0, 100))
    war.addViking(viking)

# Crear 5 Saxons y agregarlos a la guerra
for _ in range(5):
    saxon = Saxon(100, random.randint(0, 100))
    war.addSaxon(saxon)

round = 1  # Contador de rondas
while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    war.vikingAttack()
    war.saxonAttack()
    print(f"________________Round   {round} ______________________  \nViking army: {len(war.vikingArmy)}                        Saxon army: {len(war.saxonArmy)}")
    print(war.showStatus())
    round += 1
