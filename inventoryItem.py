# This class creates InventoryItem objects, assigning them names and quantities  

class InventoryItem:

    # Constructor for InventoryItem objects
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity


    # Returns the name of the item
    def name(self):
        return self._name


    # Sets the name for the item
    def setName(self, newName):
        self._name = newName


    # Returns how many of this object exist
    def quantity(self):
        return self._quantity


    # Sets a new quantity of items
    def adjustQuantity(self, newQuantity):
        self._quantity = newQuantity