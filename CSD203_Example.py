class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Menu:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_item(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_menu(self):
        if self.is_empty():
            print("Menu is empty.")
        else:
            current = self.head
            print("Menu:")
            while current:
                print(current.data)
                current = current.next


# Create a menu
menu = Menu()

# Add items to the menu
menu.add_item("Burger")
menu.add_item("Pizza")
menu.add_item("Salad")

# Display the menu
menu.display_menu()
