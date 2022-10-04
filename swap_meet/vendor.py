class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        #Adds item to the vendor's inventory
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        #Removes item from the vendor's inventory if it is in the inventory list
        else:
            self.inventory.remove(item)
            return item
    
    def get_by_category(self, category):
        #Returns a list of the vendor's items that have the same category as the argument
        items = [item for item in self.inventory if category == item.category]
        return items

    def swap_items(self, other_vendor, self_item, other_vendor_item):
        if self_item in self.inventory and other_vendor_item in other_vendor.inventory:
            #Adds vendor2's swap item and removes vendor's swap item from vendor's inventory
            for single_item in self.inventory:
                if single_item == self_item:
                    self.inventory.append(other_vendor_item)
                    self.inventory.remove(self_item)
            #Adds vendor's swap item and removes vendor2's swap item from vendor2's inventory
            for single_item in other_vendor.inventory:
                if single_item == other_vendor_item:
                    other_vendor.inventory.append(self_item)
                    other_vendor.inventory.remove(other_vendor_item)
            return True
        #Returns false if vendor's swap item is not in vendor's inventory 
        #or if vendor2's swap item is not in vendor2's inventory
        else:
            return False
