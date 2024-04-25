# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:  	L5Q1dl.py
# ------------------------------------
# Purpose: The Purpose of this program is to draw a user pompeted playing card, of any suit, from Ace to 9

def draw_top(rank):
    print(" " + 7*"_")
    print("|" + rank + 6*" " + "|") 

# Purpose: This function will draw the number of symbols indicated (between zero to three) on one line
def draw_symbols(num, symbol):
    if num == 1:
        print("|" + " "*3 + symbol + " "*3 + "|")
    elif num == 2: 
        print("|" + " " + symbol + " "*3 + symbol + " " + "|")
    elif num == 3:
        print("|" + " " + symbol + " " + symbol + " " + symbol + " " + "|")
    else:
        print("|" + " "*7 + "|")

# Purpose: This function will call draw symbols 3 times to develop the body of the card.
def draw_mid(num_outer, num_mid, symbol):
    draw_symbols(num_outer, symbol)
    draw_symbols(num_mid, symbol)
    draw_symbols(num_outer, symbol)

# Purpose: This function will print the bottom border of the card followed by the card rank between the two edge borders all on the same line
def draw_bot(rank):
    print("|" +  6*"_" + rank + "|") 
    print("")

# Purpose: This function will prompt the user for a card rank between 1 (Ace) to 9 and return the rank as a string.
def rank_input():
    rank = input("Enter a card rank (A - 9): ")
    match rank:
        case "1"  | "a":
            return "A"
        case _:
            return rank

# Purpose this function will prompt the user for a card suit C=Clubs, S=Spades, D=Diamonds, H=Hearts
def suit_input():
    suit = input("Enter suit (C, D, H, S): ").upper()
    while True:
        match suit:
            case "C":
                return "\u2664"
            case "D":
                return "\u2666"
            case "H":
                return "\u2665"
            case "S":
                return "\u2660"
            case _:
                suit= input("-> Invalid - try again: ").upper()

# Purpose: This function determines the logic of the program, utilizing the helper functions to draw playing cards of any suit from ace to 9.
def main():
    rank = rank_input()
    suit = suit_input()
    draw_top(rank)
    match rank:
        case "A":
            draw_mid(0,1,suit)
        case "2":
           draw_mid(1,0,suit) 
        case "3":
            draw_mid(1,1,suit)
        case "4":
            draw_mid(2,0,suit)
        case "5":
            draw_mid(2,1,suit)
        case "6":
            draw_mid(2,2,suit)
        case "7":
            draw_mid(2,3,suit)
        case "8":
            draw_mid(3,2,suit)
        case "9":
            draw_mid(3,3,suit)
    draw_bot(rank)

main()

# This helper function tests all posssible card combinations given, in order for it to work, main must be allowed to recieve 2 arguments (rank and suit) 
# and subsequently the lines that define them at the beginning of main must also be commented out.
#def test_draw_card():
#    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9"]
#    suits = ["C", "D", "H", "S"]
#
#    def symbolizer():
#        match suit:
#            case "C":
#                return "\u2664"
#            case "D":
#                return "\u2666"
#            case "H":
#                return "\u2665"
#            case "S":
#                return "\u2660"
#
#    for rank in ranks:
#        for suit in suits:
#            print(f"Testing main with rank={rank} and suit={suit}")
#            main(rank, symbolizer())
#            print("")

#test_draw_card()
