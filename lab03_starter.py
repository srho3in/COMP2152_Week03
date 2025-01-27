# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

# TODO: Use list() and range() to create a list of dice values ([1, 2, 3, 4, 5, 6]) instead of the current hard-coded dice values. These dice will determine the strength of the hero and the monster in battle. 
# diceOptions = [1, 2, 3, 4, 5, 6]
diceOptions = list(range(1,7))
print(diceOptions)

dicRange = range(1,4)
diceList = list(dicRange)
# for d in dicRange:
#    print(d)
#
#print(dicRange)
#print(diceList)

# TODO: Use a for loop with the in keyword to iterate over the weapons array and display the available weapons to the player.
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"] 
print ("Weapons available:")

i = 1
for w in weapons:
    print(f"{i}. {w}")
    i+=1

# TODO: Ask the player to input an integer between 1 and 6 for their combat strength (combatStrength) and monster combat strength (mCombatStrength). Validate the input to ensure it's an integer between 1 and 6. If the input is invalid, prompt the user again.
j = 0
while j < 5:
    print("Hello")
    j += 1


combatStrength = input("Enter your combat Strength: (Number between 1-6) ")
isValid = combatStrength.isnumeric() and int(combatStrength) >= 1 and int(combatStrength) <= 6

while not isValid:
    print("Input must be a number between 1 and 6")
    combatStrength = input("Enter your combat Strength: (Number between 1-6) ")
    isValid = combatStrength.isnumeric() and int(combatStrength) >= 1 and int(combatStrength) <= 6

combatStrength = int(combatStrength)

#

mCombatStrength = input("Enter the monster's combat Strength: (Number between 1-6) ")
isValid = mCombatStrength.isnumeric() and int(mCombatStrength) >= 1 and int(mCombatStrength) <= 6

while not isValid:
    print("Input must be a number between 1 and 6")
    mCombatStrength = input("Enter the monster's combat Strength: (Number between 1-6) ")
    isValid = mCombatStrength.isnumeric() and int(mCombatStrength) >= 1 and int(mCombatStrength) <= 6

mCombatStrength = int(mCombatStrength)

input("Roll the dice for your health points (Press enter)")
healthPoints = random.choice(diceOptions)
print("You rolled " + str(healthPoints) + " health points")

input("Roll the dice for the monster's health points (Press enter)")
mHealthPoints = random.choice(diceOptions)
print("You rolled " + str(mHealthPoints) + " health points for the monster")

input("Roll the dice to see if you find a healing potion (Press enter)")
healingPotion = random.choice([0, 1])
print("Have you found a healing potion?: " + str(bool(healingPotion)))

# Roll the dice (1-6) to choose which weapon you must use. Save the roll in a variable called weaponRoll.
weaponRoll = random.choice([0, 1])
    
# Add your weaponRoll to the hero's combat strength
combatStrength += weaponRoll

# Use this variable as an index into the weapons array and print out the name of the hero's weapon.
print("The name of the hero's weapon is: " + weapons[weaponRoll])

# if weaponRoll is less than or equal to 2, print out "You rolled a weak weapon, friend".
if (weaponRoll <= 2):
    print("You rolled a weak weapon, friend")
# But if weaponRoll is less than or equal to 4, print out "Your weapon is meh"
elif (weaponRoll <= 4):
    print("Your weapon is meh")
# Else, print out "Nice weapon, friend! "
else:
    print("Nice weapon, friend! ")

# If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
if (weapons[weaponRoll] != "Fist"):
    print("Thank goodness you didn't roll the Fist...")

input("Analyze the roll (Press enter)")
# Equality operators
print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

# Relational operators
print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

# and keyword
print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

# not keyword
print("--- Phew, you have a healing potion: " + str(
    not (                               # monster will NOT kill hero in one blow
        healthPoints < mCombatStrength  # monster will kill hero in one blow
    )
    and
    healingPotion == 1                  # hero has a healing potion
))

# or keyword
print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

# in keyword
print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

# --- Expanded if statement
if healthPoints >= 5:
    print("--- Your health is ok")
elif healingPotion == 1:
    healingPotion = 0
    healthPoints = 6
    print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
else:
    print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")


# --- Nested if statement
print("You meet the monster. FIGHT!!")
input("You strike first (Press enter)")

print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
if combatStrength >= mHealthPoints:
    mHealthPoints = 0
    print("You've killed the monster")
else:
    mHealthPoints -= combatStrength

    print("You've reduced the monster's health to: " + str(mHealthPoints))

    print("The monster strikes!!!")
    print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
    if mCombatStrength >= healthPoints:
        healthPoints = 0
        print("You're dead")
    else:
        healthPoints -= mCombatStrength
        print("The monster has reduced your health to: " + str(healthPoints))
print("Hello World!")