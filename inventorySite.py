# This class creates InventorySite objects, assigning them names and an inventory list

class InventorySite:

    from inventoryItem import *

    # Constructor for InventorySite objects
    def __init__(self, siteName):
        self._name = siteName
        self._inventoryList = []


    # Returns the name of the inventory site
    def siteName(self):
        return self._name


    # Sets the name of the inventory site
    def setSiteName(self, newName):
        self._name = newName


    # Adds item to the site inventory
    def addToInventory(self, item):
        self._inventoryList.append(item) # adds item to inventory list
        self._inventoryList.sort() # sorts list to alphabetic order


    # Returns site inventory list
    def getSiteInventory(self):
        return self._inventoryList


    # Prints every single item within the site's inventory list
    def printSiteInventory(self):
        print("Inventory for ", self.siteName)
        for item in self._inventoryList:
            print(item.name,"Quantity: " item.quantity "\n")