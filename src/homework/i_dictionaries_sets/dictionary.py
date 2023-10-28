inventory_dictionary = {}

def add_inventory(widget_name, quantity):
    if widget_name in inventory_dictionary:
        inventory_dictionary[widget_name] += quantity
    else:
        inventory_dictionary[widget_name] = quantity

def remove_inventory_widget(widget_name):
    if widget_name in inventory_dictionary:
        del inventory_dictionary[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'

def get_inventory():
    return inventory_dictionary



