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
    print("What are your logistical desires today? Please select from the follwing:")
    print('CREATE; create an item or inventory site \
            EDIT; edit item name or quantity or change site name \
            DELETE; remove an item or site from system WARNING deleting a site deletes all of its inventory \
            VIEW; view inventory for specified site or for all sites \
            TRANSFER; transfer items from one site to another \
            EXIT; exit from the system')