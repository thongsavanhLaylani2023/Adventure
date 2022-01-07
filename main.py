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
     print("You're not that guy, pal. Trust me, you're not that guy.")
     exit()
points = points - strength
print("Wow such stronk! STRENGTH SET TO " + str(strength))
print("You have " + str(points) + " skill points remaining.")

intelligence = int(input("How intelligent are you? (0-100)\n>"))
if intelligence > 100 or intelligence < 0 or intelligence >points:
    print("You're not that guy, pal. Trust me, you're not that guy.")
    exit()
points = points - intelligence
print("I bow down to your smarts! INTELLIGENCE SET TO " + str(intelligence))
print("You have " + str(points) + " skill points remaining.")

dexterity = int(input("How dextrous are you? (0-100)\n>"))
if dexterity > 100 or dexterity < 0 or dexterity > points:
    print("You're not that guy, pal. Trust me, you're not that guy.")
    exit()
points = points - dexterity
print("Your skills amaze me! DEXTERITY SET TO " + str(dexterity))
print("You have " + str(points) + " skill points remaining.")

wisdom = int(input("How wizzy are you? (0-100)\n>"))
if wisdom > 100 or wisdom < 0 or wisdom > points:
    print("You're not that guy, pal. Trust me, you're not that guy.")
    exit()
points = points - wisdom
print("What a wiz! WISDOM SET TO " + str(wisdom))
print("You have " + str(points) + " skill points remaining.")

charisma = int(input("How charismatic are you? (0-100)\n>"))
if charisma > 100 or charisma < 0 or charisma > points:
    print("You're not that guy, pal. Trust me, you're not that guy.")
    exit()
points = points - charisma
print("How charming! CHARISMA SET TO " + str(charisma))
print("You have " + str(points) + " skill points remaining.")
print(">")

#Race/Species

#Class
print("Now that you have your skill points assessed, it's time to choose your class, adventurer!")
print("Blademaster - A student of the sword, blademasters are one with the weapon they wield." + 
    " Weapons they can handle are swords either one-handed or dual-wield. Blademasters are mainly " + 
        "attack based and are experts in close combat. However, they're vulnerable to ranged attacks" + 
            " and have a low defense.\n>")
print("Sorcerer - One born with the gift of magic, sorcerers have magical energy flowing all " + 
    "throughout their body. They need not any weapon other than themselves, but some sorcerers " + 
        "wield staffs, sceptors, and spellbooks as tools for battle. They are mainly meant to serve " + 
            "as support in the battlefield, and are experts in long-range attacks. However, they're" + 
                " vulnerable to close-range attacks and have low agility and speed.\n>")
print("Assassin = A lone wolf who knows nothing of others but themselves, assassins are one with " + 
    "the shadows. Their weapons of choice includes daggers (dual-wielded or not), and sometimes " + 
        "scythes. They are mainly stealth-based individuals who take part in both close and ranged combat."
        + " However, they are vulnerable to both close-range attacks and ranged attacks if they are"
        + " compromised, and lack strength.\n>")
choice = input(">")

if choice.lower() == "blademaster":
    print("You have chosen Blademaster! Your starting weapon will be a dull blade with a wooden handle.")

if choice.lower() == "sorcerer":
    print("You have chosen Sorcerer! Your starting weapon will be a wooden stick. That's it. A stick.")

if choice.lower() == "assassin":
    print("You have chosen Assassin! Your starting weapon will be wood-carved daggers made from a tree.")

else:
   print("You're not that guy, pal. Trust me, you're not that guy.")
   exit()



#Prologue
print("You start off your adventure with a humble attitude. You'd finally managed to leave "
+ "your small no-name town and now you spend your days following a troupe of animal trainers "
+ "that have accepted you into their group wholeheartedly. Now with that sense of comradery that"
+ " you never had back at home, a strange confidence can be felt through your veins. The troupe"
+ " includes a generous amount of seventeen people, excluding you. The animals are bred and taught"
+ " to be fighters and protectors, as well as your everyday housepet. You've known these people for"
+ "nearly two weeks now, having spent all that time together on the road. The troupe is headed for"
+ " the famous capital, Breath Mint Gelato, where they will set home base. You are headed for-.."
+ " Well... You don't know yet. So far you've been following the animal trainers along and haven't"
+ " really decided anything for yourself other than the decision to leave your hometown. " + 
" As the night draws closer, you all sit by the campfire as traditional folk songs are sung and" + 
" stories of hardship are told through the comradery that has been built. The leader of the troupe"
+ " pulls you aside far from the campfire. He is Matty. A young boy about the same age, if not younger, than you."
+ " His aunt was the former leader but she has since passed and given the legacy to him a year or so ago."
+ " Matty asks you a question that has been on your mind since you met the troupe. He asks if you're"
+ " comfortable with the idea of joining them. He looks at you solemnly as he waits for your answer.")
print("\nWhat will you do?")
print("1. Accept his offer.")
print("2. Decline his offer.")
print("3. Kill Matty.")
choice = input(">")

if choice == "1":
    print("You tell Matty that you would love to join his troupe. With the time that you've spent"
    + " together, you've grown to like animal training. The boy is satisfied with your answer."
    + " He gives a sigh of relief and pats you on the back, whispering his thank-you's before"
    + " going back to the campfire and offering another round of drinks to the group. He seems to be"
    + " in a good mood. Now that you have joined the troupe, you are on your way to Breath Mint"
    + " Gelato, the capital. You will stay with the troupe and spend your life training the animals"
    + " to become sworn fighters and protectors. Finally apart of something, you feel that your"
    + " short, two-week, adventure has served its purpose.")
    print("GAME OVER\n'FRIENDSHIP GOES A LONG WAY' ENDING")
    exit()


elif choice == "2":
    print("You tell Matty that you have to decline, but are thankful that he gave you the offer."
    + " The boy, albeit visibly disappointed with your answer, nods his head and pats your shoulder"
    + " in understanding. He asks if you'd like the troupe to drop you off and part ways at the capital"
    + ", but you decline as well and tell him you will be leaving the troupe tomorrow, as your"
    + " separation from each other has since long been overdue. He nods again before patting you on the back"
    + " and walking back to the campfire to sit with his dog quietly as the troupe enjoys the rest"
    + " of the night.")

elif choice == "3":
    print("For some reason, you have the sudden urge to murder Matty, your dearest friend on the trip."
    + " I mean, what does this cockly little mf think he's saying, asking YOU to join a troupe"
    + " of some dumb.. what.. ripoff Pokemon Trainers? You pull out your weapon and in an effort to "
    + "kill him, you lunge the sharpest end of your weapon at his throat. However, Matty's dog"
    + " senses your advances from afar and the rest of the troupe's animals pounce on you, chewing,"
    + " gnawing, and viciously attacking your guts. They maul you to death for trying to kill their"
    + " master.")
    print("YOU DIED")
    exit()

else: 
    print("You're not that guy, pal. Trust me, you're not that guy.")
    exit()


#Post-Prologue
print("")
print("\nThe next morning, you prepare yourself to leave, though there's not much to do in the first place."
+ " All you had on you was a leather backpack full of the bare necessities such as spare clothes,"
+ " kettle of water, some food from the torupe, and so on. The other members have heard wind of your"
+ " departure and they gather outside their carriages, chattering about as they wait for your packing"
+ " to end. When you finally step outside of your tent, they all surround you and give you tearful"
+ " goodbyes that harbor the emotions they carry from your time together. As the time comes for you to leave,"
+ " Matty is the last one to say goodbye. He puts his hand on your shoulder and tells you that you will"
+ " always have a home with the animal training troupe in Breath Mint Gelato if you so desire")
print("")
print("With that, you seperate from the group and set off in the woods, not following any trails as"
+ " you believe fate will lead you somewhere like the idiot that you are.")

#First Encounter and More
print("")
print("Luckily, you reach a crossroads where there is a sign stating directions that you can take.")
print("\nWhere will you head for?")
print("1. The capital, Breath Mint Gelato, the road is full of dangers and monsters")
print("2. The first neighboring town, Arceus, the road is full of tricks")
print("3. The second neighboring town, Melty, the road is known to be difficult to traverse on")
print("4. None of them. Follow your wits.")
choice = input(">")

if choice == "1":
    roll = random.randrange(0, strength)
    if roll > 40:
        print("You decide to take the long road to the capital despite the dangers that lurk."
        + " Luckily, you manage on your way there and defeat the many monsters, bandits, and overrall"
        + " enemies that threaten your wellbeing. You continue down the road after the path is cleared"
        + " and after what's been five days you finally make it to the capital. You sold off the"
        + " loot that you gathered from killing enemies and make a solid amount of money."
        + " Though not rich, you can buy better equipment with it.")
        print("")
        print("What will you do?")
        print("1. Shop for equipment")
        print("2. Find a place to stay")
        print("3. Leave Breath Mint Gelato")
        choice = input(">")

        if choice == "1":
            print("You head to the local market. Thankfully, you're in the capital so only the best"
            + " of the best are here.")

        elif choice == "2":
            print("You choose to look for a place to stay in the Capital. Everything is a bit pricy"
            + " here due to this being the capital, so the prices are inflamed. However, you find a"
            + " decent enough hotel to stay in, but some of the locals tend to avoid this place.")
            print("Will you stay here?")
            print("1. Yes")
            print("2. No")
            choice = input(">")

            if choice == "1":
                print("You decide to stay in the shady hotel. Pickign out a room, you unpack your belongings"
                + " and leave to find a tavern but are jumped by a group of bandits outside your room and die.")
                print("YOU DIED")
                exit()

    else:
        print("You decide to take the long road to the capital despite the dangers that lurk."
        + " Unluckily, you die after your first encounter with a monster.")
        print("YOU DIED")
        exit()

elif choice == "2":
    roll = random.randrange(0, wisdom)
    if roll > 30:
        print("You decide to take the short road to the neighboring town Areus despite the tricks."
        + " Thanks to your wisdom, you manage to avoid the tricks that threaten you and safely"
        + " make your way to Arceus. Though, once you got there, you realized you didn't have"
        + " any money to spend on better equipment. Thankfully, you have your pack full of"
        + " food, water, and your tent, but that's not enough for you to survive." +
        " You do, however, find that Arceus is a nice place to reside in despite not having the means"
        + " to live there. You're gonna have to get money.")

    else:
        print("You decide to take the short road to the neighboring town Arceus despite the tricks."
        + " However, you don't have good enough judgement, experience, or knowledge of such to"
        + " survive and end up getting tricked by a nymph and die.")
        print("YOU DIED")
        exit()

elif choice == "3":
    roll = random.randrange(0, dexterity)
    if roll > 20:
        print("You decide to take the short road to the neighboring town Melty despite how difficult"
        + " it's known to be. There are many vines and stones that you have to climb up in order to"
        + " make it to Melty safely. Thankfully, the vines aren't too rough for you and you manage."
        + " After two days you make it to Melty and are greeted by the town mayor. He seems to be"
        + " a plump, confident, man resembling an apple. His mustache catches you off guard,"
        + " but other than that he gladly welcomes you to Melty. The mayor asks how long you're staying"
        + " and if you need a room at the luxorious boujee hotel that they have. However, you realize"
        + " you don't have any money and break the news to the mayor. Upon hearing this, he immediately"
        + " grimaces and tells you that he has no room for *your* kind in Melty. The mayor leaves you in"
        + " the town square. You notice a small beggar girl watching you from the alleyways.")

    else:
        print("You decide to take the short road to the neighboring town Melty despite how difficult"
        + " it's known to be. There are many vines and stones that you have to climb up in order to"
        + " make it to Melty sasfely. Unfortunately, whilst climbing one of the vines hanging"
        + " off of a mountain's cliff, you misplace your hands and end up falling to your death.")
        print("YOU DIED")
        exit()

elif choice == "4":
    roll = random.randrange(0, wisdom)
    if roll > 45:
        print("You decide not to take any of the set paths and follow your wits as well as your heart."
        + " A few days in, you start to lose hope and feel that you are lost. However, just as you"
        + " were about to give up and face your death, you notice an iridescent glowing light shining"
        + " in the distance. Following the glowing lights you are met with an ethereal cave. Maybe"
        + " this is a treasure?")
        print("")
        print("Make a choice.")
        print("1. Enter the cave")
        print("2. Stare at the cave")
        print("3. Destroy the cave")
        choice = input(">")

        if choice == "1":
            print("Entering the cave cautiously, you are taken in by the magical atmosphere that"
            + " surrounds you and suffocates your lungs, squeezing them in a way that feels"
            + " threatening yet exciting. There are glowing crystals that line the cave beautifully,"
            + " as if made of rich material. There's a low hum that purrs throughout the cave,"
            + " causing a chilling vibration in your body. The hum begins to emanate breathing."
            + " As you venture further into the cave there is a ring that shines ever so"
            + " lusciously, as if waiting for you.")
            print("")
            print("What will you do?")
            print("1. Take the ring")
            print("2. Destroy the ring")
            print("3. Leave")
            choice = input(">")

        elif choice == "2":
            print("Too wary to enter the cave, you stare at it. Waiting for something out of fear of"
            + " danger. You wait, and wait, and wait.. But nothing happens. Once you finally"
            + " decide to enter the cave, the entrance behind you is closed due to the"
            + " eruptuous collapsing of rocks and land above. When you turn back to try and break the rocks"
            + ", a loud growl catches you off guard. Before you can turn to see what's causing it,"
            + " you are enraptured in a warm interior and you can feel your bones being crushed as"
            + " sharp teeth break through your flesh, killing you.")
            print("YOU DIED")
            exit()

        elif choice == "3":
            print("For some reason, you set your mind to destroy the cave. In your pack you take out"
            + " explosives given to you by the troupe and set them atop the rocks of the cave as well as"
            + " inside and around it. You detonate the bombs, causing an explosion similar to that of"
            + " an avalanche. Rocks fall and gather on the ground, the cave collapses and the glowing"
            + " light is no more. Satisfied, you're set to turn away and leave but a loud and low"
            + " rumbling is heard beneath the rubble, a set of wings and fiery aura catches your eye."
            + " A dragon, Khaen'ra, looks at you fiercely. He's angered at how you destroyed his"
            + " beautiful home and is set on killing you.")
            print("")
            print("What's your next move?")
            print("1. Fight")
            print("2. Run")
            print("3. Talk")
            print("4. Give up")
            choice = input(">")

            if choice == "1":
                roll = random.randrange(0, strength)
                if roll > 90:
                    print("You use your overpowing strength to kill the dragon, and through a"
                    + " tough battle with bloodshed from both sides, you win. Having defeated"
                    + " the dragon Khaen'ra, you feel good about yourself. If you take some"
                    + " spoils of the battle, you'll be seen as the world's hero, won't you?")
                    print("GAME OVER\n'HERO' ENDING")
                    exit()

                else:
                    print("You attempt to fight the dragon Khaen'ra, but you're too weak. He laughs and"
                    + " growls with pity for you before devouring you alive without leaving a single"
                    + " trace of you on this world.")
                    print("YOU DIED")
                    exit()

            elif choice == "2":
                roll = random.randrange(0, dexterity)
                if roll > 90:
                    print("Knowing that you are not strong enough to fight the dragon Khaen'ra, you run"
                    + " for your life like the lowly coward that you are. Thankfully, you manage to"
                    + " escape his sights. However, you find yourself stuck in a slime swamp."
                    + " You remember from your common sense that slime swamps are simiar to quick sand."
                    + " You struggle to find a way out and are consumed by the slimes, suffocating to"
                    + " your death.")
                    print("YOU DIED")
                    exit()

                else:
                    print("Knowing you are not strong enough to fight the dragon Khaen'ra, you run"
                    + " for your life like the lowly coward taht you are. However, you are not"
                    + " swift enough to outrun and escape the dragon, thus making yourself easy prey."
                    + " He easily picks you up with his claws and viciously drops you to your death.")
                    print("YOU DIED")
                    exit()

            elif choice == "3":
                roll = random.randrange(0, charisma)
                if roll > 90:
                    print("You decide to use your charismatic sense and talk to the dragon. You tell"
                    + " him a lot of words and stuff. The dragon seems to be touched, but says that"
                    + " it doesn't change the fact that you destroyed his home. He huffs angrily"
                    + " and you quickly try to feed the dragon Khaen'ra excuses, but he isn't"
                    + " having it and incinerates you with fire.")
                    print("YOU DIED")
                    exit()

                else:
                    print("You try to talk to the dragon Khaen'ra, but you stumble over your words"
                    + " and he deems you stupid. Thinking the world would be better off with such"
                    + " a dumb person like you, he kills you ruthlessly. Without regret.")
                    print("YOU DIED")
                    exit()

            elif choice == "4":
                print("You decide to give yourself up to the dragon and face death. Thinking you're brave"
                + " for this, the dragon Khaen'ra says he'll give you an honorable death and eats you."
                + " At least it was honorable.")
                print("YOU DIED")
                exit()

            else:
                print("You're not that guy, pal. Trust me, you're not that guy.")
                exit()

    else:
        print("You decide not to take any of the set paths and follow your wits as well as your heart."
        + " After a week of wandering, you are at a loss. You have no more food,  no more water, and"
        + " haven't seen a human in the last eight days. You decide to give up.")
        print("YOU DIED")
        exit()

else:
    print("You're not that guy, pal. Trust me, you're not that guy.")
    exit()






