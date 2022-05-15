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

    



# Method allows user to edit name of site or item or quantity of item
def edit():
    while(True):

        userInput = input("Would you like to change the NAME or QUANTITY of an item? or EXIT\n")

        if userInput.lower() == "exit": # User wishes to return to menu
            break

        elif userInput.lower() == "name" or userInput.lower() == "quantity":
            itemName = input("Which item would you like to edit?\n")
            itemExists = False
            updated = False

            for location in sites: # Check if item exists
                for item in location.getSiteInventory():
                    if item.name().lower() == itemName.lower():
                        itemExists = True


                        if userInput.lower() == "name": # User wishes to change item name
                            newName = input("What is the desired new name of " + itemName.lower() + "\n")

                            for site in sites: # Changes item name across all sites
                                for obj in site.getSiteInventory():
                                    if obj.name().lower() == itemName.lower():
                                        item.setName(newName)
                                        updated = True
                            print(itemName.lower() + " shall now be called " + newName + "\n")
                          


                        elif userInput.lower() == "quantity": # User wishes to change item quantity
                            site = input("Which site would you like to adjust quantity of " + itemName + "?\n")
                            siteExists = False

                            for warehouse in sites: # Check if site exists
                                if site.lower() == location.siteName().lower():
                                    siteExists = True
                                    siteItemExists = False
                                    for inventory in warehouse.getSiteInventory(): # Checks if item exists at given site
                                        if inventory.name().lower() == itemName.lower():
                                            try: # Ensures user enters integer value
                                                newQuantity = input("What is the desired quantity of " + itemName + "?\n")

                                            except:
                                                print("Invalid entry. Please enter an integer value. \n")

                                            else: # Change the quatnity of the item at given site
                                                siteItemExists = True
                                                inventory.adjustQuantity(newQuantity)
                                                print(warehouse.siteName() + " now has " + newQuantity + " " + itemName + "\n")
                                            break

                                    if not siteItemExists:
                                        print("No such item exists at this site.")

                            if not siteExists:
                                print("No such site exists.")

                        else:
                            print("Invalid option, try again.\n")
                
                if updated:
                    break  
                                    
            if not itemExists:
                print("No such item exists.")          
        
        else:
            print("Invalid option, try again.")

        



# Removes entered inventory item from all sites
def delete():
    while(True):

        userInput = input("Which item would you like to delete? of EXIT\n")

        if userInput.lower() == "exit":# User wishes to return to menu
            break

        else:
            for site in sites: # Loop through sites and delete item
                site.removeItemFromInventory(userInput)
            print(userInput + " no longer exists at any inventory site.")
            break






#def view():
 #   while(True):

    
# Runs code
main()