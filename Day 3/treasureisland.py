print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("🏝️ Welcome to *Treasure Island* 🏝️")
print("Your mission is simple: **Find the hidden treasure!** 💰")

direction = input("🚶 You're standing at a crossroad... Do you want to go **left** or **right**? 👉\n").strip().lower()

if direction == "left":
    print("\n🌊 You've arrived at a shimmering lake. In the middle lies a mysterious island...")
    choice = input("⛵ Do you **wait** for a boat or do you **swim** across? (type 'wait' or 'swim')\n").strip().lower()

    if choice == "wait":
        print("\n⛴️ A boat arrives and safely takes you across the lake. You step onto the island... 🏝️")
        doors = input(
            "🚪 You see three doors in front of a stone temple: one **Red**, one **Blue**, and one **Yellow**. Which do you choose?\n").strip().lower()

        if doors == "red":
            print("🔥 The door bursts into flames as you enter... You've been burned alive. 💀 *Game Over!*")
        elif doors == "blue":
            print("🐺 You enter a dark room filled with hungry beasts... You never stood a chance. 💀 *Game Over!*")
        elif doors == "yellow":
            print(
                "🏆 You open the golden door and find the legendary treasure chest overflowing with gold! 🎉 *Congratulations! You Win!*")
        else:
            print("🚫 That's not a valid door... a trapdoor opens beneath you. 😵 *Game Over!*")
    else:
        print("🦈 As you swim, a shark circles in... You're pulled underwater. 💀 *Game Over!*")
else:
    print("🕳️ You take a step and fall into a hidden pit. Ouch! 💀 *Game Over!*")