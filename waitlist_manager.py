# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
            return f"{name} added to the end of the waitlist"

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        if self.head is None:
            return f"{name} not found"

        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return f"Removed {name} from the waitlist"
            current = current.next

        return f"{name} not found"

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        current = self.head
        while current is not None:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            print(waitlist.add_end(name))

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            print(waitlist.remove(name))

        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Call the waitlist_generator function to start the program
waitlist_generator()


'''
Design Memo:
1. How does your list work?
My LinkedList is made of Node objects, each holding a name and a pointer
called next to the following node. The list itself only keeps track of
head, a reference to the first node. Every operation, adding, removing,
or printing, works by starting at head and following next pointers until
it finds the position it needs.

2. What role does the head play?
head is the only fixed entry point into the list. Without it, there would
be no way to reach any node, since nodes only know about the node that
comes after them, not before. Adding to the front means creating a new
node and reassigning head to point to it. Removing the first customer
means moving head forward to whatever the current head's next pointer is.

3. When might a real engineer need a custom list like this?
A built-in list works fine for most cases, but a custom linked list gives
control over exactly how insertion and removal happen at the front or in
the middle, without shifting every other element in memory the way a
Python list does when you insert at index 0. That matters for something
like a live waitlist, where customers are constantly being added to the
front, added to the end, or pulled out from anywhere, and the queue needs
to update without re-copying the whole structure on every change.
'''