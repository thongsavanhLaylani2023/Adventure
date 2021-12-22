import random
#strength
#intelligence
#dexterity
#wisdom
#charisma


#Skill Points

points = 250

print("Welcome, adventurer! Skill point time! (250 skill points available)")

strength = int(input("How strong are you? (0-100)\n>"))
if strength > 100 or strength < 0 or strength > points:
    print("You can't do that! You LOSE!")
    exit()
points = points - strength
print("Wow such stronk! STRENGTH SET TO " + str(strength))
print("You have " + str(points) + " skill points remaining.")

intelligence = int(input("How intelligent are you? (0-100)\n>"))
if intelligence > 100 or intelligence < 0 or intelligence >points:
    print("You can't do that! You LOSE!")
    exit()
points = points - intelligence
print("I bow down to your smarts! INTELLIGENCE SET TO " + str(intelligence))
print("You have " + str(points) + " skill points remaining.")

dexterity = int(input("How dextrous are you? (0-100)\n>"))
if dexterity > 100 or dexterity < 0 or dexterity > points:
    print("You can't do that! YOU LOSE!")
    exit()
points = points - dexterity
print("Your skills amaze me! DEXTERITY SET TO " + str(dexterity))
print("You have " + str(points) + " skill points remaining.")

wisdom = int(input("How wizzy are you? (0-100)\n>"))
if wisdom > 100 or wisdom < 0 or wisdom > points:
    print("You can't do that! YOU LOSE!")
    exit()
points = points - wisdom
print("What a wiz! WISDOM SET TO " + str(wisdom))
print("You have " + str(points) + " skill points remaining.")

charisma = int(input("How charismatic are you? (0-100)\n>"))
if charisma > 100 or charisma < 0 or charisma > points:
    print("You can't do that! YOU LOSE!")
    exit()
points = points - charisma
print("How charming! CHARISMA SET TO " + str(charisma))
print("You have " + str(points) + " skill points remaining.")
print(">")

#Class
print("Now that you have your skill points assessed, it's time to choose your class, adventurer!")
print("Blademaster - A student of the sword, blademasters are one with the weapon they wield." + 
    " Weapons they can handle are swords either one-handed or dual-wield. Blademasters are mainly " + 
        "attack based and are experts in close combat. However, they're vulnerable to ranged attacks" + 
            " and have a low defense.\n>")

print("Sorcerer - A human born with the gift of magic, sorcerers have magical energy flowing all " + 
    "throughout their body. They need not any weapon other than themselves, but some sorcerers " + 
        "wield staffs, sceptors, and spellbooks as tools for battle. They are mainly meant to serve " + 
            "as support in the battlefield, and are experts in long-range attacks. However, they're" + 
                " vulnerable to close-range attacks and have low agility and speed.\n>")

print("Assassin = A lone wolf who knows nothing of others but themselves, assassins are one with " + 
    "the shadows. Their weapon of choice ")

#First Encounter
print("Uh oh spaghetti-o! You encounter a menacing wall blocking your path. What do you do?")
print("1. Punch wall")
print("2. Reason with wall")
print("3. Climb wall")
print("4. Magic wall")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 50:
        print("The wall shatters in awe of your divine strength.")

    else:
        print("Your fist shatters in awe of the wall's divine strength.")
        exit()

elif choice == "2":
    roll = random.randrange(0, charisma)
    if roll > 40:
        print("The wall blushes due to the charm of your words! It politely moves aside for you.")

    else:
        print("As you try to reason with the wall, it continues to stand there void of movement.." +
        " I'm not sure what you were trying to do here, but it was worth a shot.")
        exit()

elif choice == "3":
    print("cool")

elif choice == "4":
    print("cool")

else:
    print("You can't do that! You LOSE!")
    exit()



