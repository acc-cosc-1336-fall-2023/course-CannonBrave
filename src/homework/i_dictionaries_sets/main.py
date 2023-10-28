from dictionary import add_inventory, remove_inventory_widget


while True:
    print("\nInventory Menu")
    print("1-Add or Update Item")
    print("2-Delete Item")
    print("3-Exit")
        
    choice = input("Enter your choice: ")
        
    if choice == "1":
        widget_name = input("Enter widget name: ")
        quantity = int(input("Enter quantity: "))
        add_inventory(widget_name, quantity)
        print(f"{widget_name} updated in the inventory.")
        
    elif choice == "2":
        widget_name = input("Enter widget name to delete: ")
        response = remove_inventory_widget(widget_name)
        print(response)
        
    elif choice == "3":
        break
        
    else:
        print("Invalid choice. Please select from the menu.")


