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
    print("\nHello! Welcome to Geek Emporium!\n")
    print("What are your logistical desires today? Please select from the following: \n")
    print("CREATE;      create an item or inventory site \n"
            "EDIT;      edit item name or quantity or change site name \n"
            "DELETE;        remove an item or site from system WARNING deleting a site deletes all of its inventory \n"
            "VIEW;      view inventory for specified site or for all sites \n"
            "TRANSFER;      transfer items from one site to another \n"
            "EXIT;      exit from the system\n")


main()