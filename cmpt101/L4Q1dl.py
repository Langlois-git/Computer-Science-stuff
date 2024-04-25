# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:  	L4Q1dl.py
# ------------------------------------
# Purpose:  The purpose of this program is to classify a user defined food item into 1 of 6 catergories.
count = 0
ans = ""

step  = int(input("Enter Number (1 to 10): "))
while not (0 < step <= 10):
    step = int( input("-> Error! Try again: "))

print("")
count_direction = input("Count up or down (U or D): ").lower()
while (count_direction != "u") & (count_direction != "d"):
    count_direction = input("-> Invalid! Try again: ").lower()

print("")
print("What is the missing number?")

match count_direction:
    case "u" :
       start_multi = -1
       stop = 5
       step_multi = 1
       
    case "d":
        start_multi = 1
        step_multi = -1
        stop = 10

for i in range(0, stop):
    if i == 4:
        print((step * start_multi * 5 + 1) + (step_multi*count*step), end = " ")
        print("_", end = " ")
        count += 2
    else:
        print((step * start_multi * 5 + 1) + (step_multi*count*step), end = " ")
        count += 1

print("")
print("")
while (ans != "y") & (ans != "n"):
    ans = input("Show answer (y or n)? ").lower()

if ans == "y":
    print("Answer: 1")