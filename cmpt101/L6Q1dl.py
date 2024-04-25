# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:  	L6Q1dl.py
# ------------------------------------
# Purpose: This program will analyze a password provided by the user


# Purpose: get_password prompts the user to input a password, error checking to ensure the length is longer than 9
def get_password():
    print("")
    passw = input("Enter a password (minimum 10 chars): ")
    while len(passw) < 10:
        passw = input("-> Too short! Try again: ")
    return passw

# Purpose: check_flaws informs the user if their password has a digit, a special character, an uppercase character and a lowercase character
def check_flaws(string):
    print("")
    digit = 0
    lowchar = 0
    spechar = 0
    upchar = 0
    for char in string:
        if char.isupper():
            upchar += 1
        elif char.islower():
            lowchar += 1
        elif char.isdigit():
            digit += 1
        else:
            spechar += 1

    flaw_count = 4 - (bool(digit) + bool(lowchar) + bool(spechar) + bool(upchar))
    print(f"Flaw check:\t {string} has {flaw_count} flaw(s)")
    if not upchar:
        print("-> No uppercase chars")
    if not lowchar:
        print("-> No lowercase chars")
    if not digit:
        print("-> No digits") 
    if not spechar:
        print("-> No special chars")

# Purpose: show_stats diplays some Statistics about indexs of the password 
def show_stats(string):
    print("")
    print("Statistics for: ",string[:1]+"*"*(len(string)-1)) 
    print(f"(a) Length:\t {len(string)} characters")
    print(f"(b) Fifth char:\t {string[4]}")
    print(f"(c) Last two chars: {string[-2:]}")

# {urpose: hash_swap returns a hash of the password and then generates a new hash for a new version of the password 
def hash_swap(string):
    print("")
    print(f"(d) Hash generated:\t {hash(string)}")
    if len(string) >= 4:
        new_string = string[2:4] + string[:2] + string[4:]
        print(f"(e) Two pairs swappped:\t {hash(new_string)}")

# Purpose: examine_passsword defines the logic of the password checker
def examine_passsword():
    password = get_password()
    check_flaws(password)
    show_stats(password)
    hash_swap(password)

examine_passsword()