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

    # Greeting and options menu
    print("\nHello! Welcome to Geek Emporium!\n")
    print("What are your logistical desires today? Please select from the following: \n")

    userInput = input("CREATE;      create an item and assign it to an inventory site or create an inventory site. \n"
            "EDIT;      edit item name or quantity. \n"
            "DELETE;        remove an item from system WARNING deleting an item deletes all of its inventory from all sites. \n"
            "VIEW;      view inventory for specified site or for all sites. \n"
            "EXIT;      exit from the system.\n")

    while (userInput.lower() != "exit"):
        handleInput(userInput.lower())

        userInput = input("Please select from the following: \n\n"
            "CREATE;      create an item and assign it to an inventory site or create an inventory site. \n"
            "EDIT;      edit item name or quantity. \n"
            "DELETE;        remove an item from system WARNING deleting an item deletes all of its inventory from all sites. \n"
            "VIEW;      view inventory for specified site or for all sites. \n"
            "EXIT;      exit from the system.\n")

    print("Thank you for using Geek Emporium, have a nerdy day!") # User exited



# Redirects user after input from menu
def handleInput(input):
    
    if input == "create": # User wishes to create item/site
        create()

    elif input == "edit": # User wishes to edit item
        edit()

    elif input == "delete": # User wishes to delete item
        delete()

    elif input == "view": # User wishes to view inventory
        view()
    
    else:   # User entered invalid option
        print("Invalid selection, please try again. \n")



# Method to create either a new site or a new item and add it to a site
def create():
    while(True): # Loops until user has created or exited

        userInput = input("Would you like to create a SITE or ITEM? or EXIT \n") 


        # User wishes to create new site
        if userInput.lower() == "site":
            createdSite = False

            while(not createdSite): # Loop until inventory site is created
                siteName = input("Please enter the name of the site you wish to create. \n")
                exists = False

                for location in sites: # Check if the site already exists
                    if siteName.lower() == location.siteName().lower():
                        print("A variation of that site name exists, please try again \n")
                        exists = True
                        break

                if not exists:   # Create new inventory site with given name
                    sites.append(InventorySite(siteName))
                    print("Site \"" + siteName + "\" created.\n")
                    createdSite = True # exit loop



        # User wishes to create new item
        elif userInput.lower() == "item":
            createdItem = False 

            while(not createdItem): # Loop until item is created
                itemName = input("Please enter the name of the item you wish to create. \n")

                try: # Ensures user enters integer value
                    itemQuantity = int(input("Please enter the number of \"" + itemName +  "s\" you wish to add to inventory. \n"))
                except:
                    print("Invalid entry. Please enter an integer value. \n")

                else:
                    added = False
                    while(not added):
                        site = input("Please enter the site in which you wish to add this inventory item. \n") 

                        for location in sites:
                            if site.lower() == location.siteName().lower(): # Checks to see if site exists
                                location.addToInventory(InventoryItem(itemName, itemQuantity)) # Creates item with given name and quantity and adds it to specified site
                                print(str(itemQuantity) + " \"" + itemName + "s\" have been added to " + location.siteName())
                                createdItem = added = True
                                break
                            print("Invalid site.\n")


        # User wishes to exit to menu
        elif userInput.lower() == "exit":
            break


        # User types invalid option                         
        else:
            print("Invalid entry. Please try again. \n")

        break # Return to menu
    



# Method allows user to edit name of site or item or quantity of item
def edit():
    while(True):

        userInput = input("Would you like to edit a SITE or ITEM? or EXIT \n")

        # User wishes to edit site
        if userInput.lower() == "site":



        # User wishes to exit to menu
        elif userInput.lower() == "exit":
            break


        # User types invalid option                         
        else:
            print("Invalid entry. Please try again. \n")

        break # Return to menu

# Runs code
main()