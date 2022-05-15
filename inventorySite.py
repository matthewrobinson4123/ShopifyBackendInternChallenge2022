# This class creates InventorySite objects, assigning them names and an inventory list

class InventorySite:


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
        self._inventoryList.sort(key=lambda item: item._name) # sorts list to alphabetic order


    # Removes item from inventory
    def removeItemFromInventory(self, item):
        newList = []
        for obj in self._inventoryList:
            if item != obj.name:
                newList.append(obj)
        self._inventoryList = newList


    # Returns site inventory list
    def getSiteInventory(self):
        return self._inventoryList
