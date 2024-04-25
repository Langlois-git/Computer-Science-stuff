# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:  	L3Q1dl.py
# ------------------------------------
# Purpose:  The purpose of this program is to classify a user defined food item into 1 of 6 catergories.

collection = ""
side_counter = 0

# This code block introduces the program
print("Cube Rule Classification System")
print("")
print("Does this food have a: ")

# This code block recieves input from the user to determine used cube sides
bottom_side = input("A) bottom side (y/n)? ").lower()
if bottom_side == "y":
    collection = collection+" B"
top_side = input("B) top side (y/n)? ").lower()
if top_side == "y":
    collection = collection+" T"
left_side = input("C) left side (y/n)? ").lower()
if left_side == "y":
    collection = collection+" L"
    right_side = input("   and a right side (y/n)? ").lower()
    if right_side == "y":
        collection = collection+" R"
front_back_side = input("D) front and back side (y/n)? ").lower()
if front_back_side == "y":
    collection = collection+" F&B"
print("")

# This code block counts the sides of the food and determines concluding scentence grammar.
for i in collection:
    if i == " ":
        side_counter += 1        
if side_counter == 1:
    print(f"Your food has {side_counter} side of a cube:{collection}")
else:
    print(f"Your food has {side_counter} sides of a cube:{collection}")

# This code block classifes the food item using the rules of cube classification    
match collection:
    case " B":
        print("You got toast!")
    case " B T":
        print("You got a sandwich!")
    case " B L R":
        print("You got a taco!")
    case " B T L R":
        print("You got sushi!")
    case " B L R F&B":
        print("You got a bread bowl!")
    case " B T L R F&B":
        print("You got a calzone!")
    case _:
        print("Your food does not fit in any category.")
        print("Perhaps your food is incorrectly oriented.")


