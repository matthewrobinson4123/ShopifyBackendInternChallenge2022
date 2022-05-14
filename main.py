############################
# Author: Matthew Robinson
# 
# Shopify Backend Developer Intern Challenge 2022
############################


# import objects
from inventoryItem import InventoryItem
from inventorySite import InventorySite


# sample items to test with
inventory = [InventoryItem("Warhammer Space Marines", 42), InventoryItem("Lego Star Destroyer", 5), InventoryItem("Settlers of Catan", 16)]

# Inistialize system
sites = [InventorySite("Geekdom")]
for item in inventory:
    sites[0].addToInventory(item)



# Logistics program, allows user to create, edit and view Inventory sites and products
def main():
    print("Hello! Welcome to Geek imporium!")
    print("")