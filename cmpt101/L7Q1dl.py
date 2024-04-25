# Integrity pledge: This submission is my own work, except where I have acknowledged the use of the works of other people. 
#-------------------------------------
#  Name:     	David Langlois
#  Program:  	L7Q1dl.py
# ------------------------------------
# Purpose: The Purpose of this program is act as a warehouse inventory shipping summary 

#The sum function in not permitted

import typing, random

def show_inventory(inventory: list):
    """prints the inventory displaying each entry in the inventory list with its list position"""

    print("")
    print("Warehouse Inventory today: ")
    for entry in inventory:
        print(f"{inventory.index(entry)}. {entry}")


def place_orders(inventory: list) -> list:
    """Creates a list of randomly generated integers to repersent orders made"""
    
    shipments = [] 
    inventory_size = len(inventory)

    print("")
    for entry in inventory:
        shipments.append(random.randint(-3*inventory_size, 3*inventory_size))
    
    print(f"Generating {inventory_size} crate orders (any number from {-3 * inventory_size} to {3 * inventory_size}):")
    print(shipments)
    return shipments

    
def display_changes(inventory: list, shipments: list):
    """Prints the inventory changes showing each item from the inventory list with its corresponding order number from the shipments list, negative numbers repersent outgoing orders and positive (or zero) repersent inbound"""

    count = 0
    
    print("")
    print("Todays crate shipments: ")
    for entry in shipments:
        if entry >= 0:
            print(f"-> {abs(entry)} crates of {inventory[count]} inbound")
            count += 1
        else:
            print(f"-> {abs(entry)} crates of {inventory[count]} outgoing")
            count += 1

            
def calc_net_change(shipments: list):
    """Calculates the net change of crates in the warehouse"""

    net_change = 0
    for entry in shipments:
        net_change = net_change + entry
    print("")
    print(f"The net change of crates in the warehouse is {net_change}.")



def warehouse_activities(inventory: list):
    """Defines the logic of the program"""

    show_inventory(inventory)
    shipments = place_orders(inventory)
    display_changes(inventory, shipments)
    calc_net_change(shipments)

# test_list = ["Tv", "Shampoo", "Hats", "Butter"]
# warehouse_activities(test_list)