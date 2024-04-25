# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:  	L2Q1dl.py
# ------------------------------------
# Purpose:  This program will recieve 5 inputs from the user and generates a short story

print("Please enter the following: ")

number = int(input("-> (1) a number (1-8): "))
city = input("-> (2) a city: ")
name = input("-> (3) a name: ")
animal = input("-> (4) an animal: ")
noun = input("-> (5) a noun: ")

print("")
print("Here's a story using your words: ")
print("")

print(f"My alarm is set for (1) {number} AM so I can get to the airport on time.")

print(f"I fly to (2) {city} three hours later at {number+3}:00 AM on flight {3*str(number)}.")

print(f"My friend (3) {name} will pet-sit my (4) {animal} while I a away.")

print(f"Uh oh! Did I forget to pack my (5) {noun}.")
