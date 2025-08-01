class LinkedList:
    # the below line is a constructor method that initializes LinkedList class.
    # Initializes with a head node containing given 'value'
    # LinkedList must be started only with a single value
    def __init__(self, value):
        self.head = {
            'value' : value , # Store the initial value in the head node
            'next' : None     # The 'next' reference starts as None (no next node)
        }
        self.tail = self.head # Since there’s only one node at initialization, both head and tail point to it
        self.length = 1       # The linked list has one item initially
        print("Hi, This is My Dictionary Based Linked List. Use Method 'help()' for listing all the methods")

    def append(self, data):
        new_node = {
            "value" : data ,
            "next" : None     # New node always ends with 'next' as None
        }
        self.tail['next'] = new_node  # Point current tail to the new node
        self.tail = new_node          # Update tail to new node
        self.length += 1              # Increment the length of the list
        return self                   # Return the updated list (chainable)

    def prepend(self, data):
        new_node = {
            "value": data,
            "next": None
        }
        new_node['next'] = self.head    # Point the new node to the current head
        self.head = new_node            # Update the head to be the new node
        self.length += 1
        return self

    def insert(self, index, value):
        new_node = {
            "value": value,
            "next": None
        }
        if index == 0:
            self.prepend(value)
            return self.print_list()

        if index >= self.length:
            self.append(value)
            return self.print_list()

        leader = self.get_index(index - 1)  # Get the node before the desired position
        next_leader = leader['next']        # Store the next node to reconnect later
        leader['next'] = new_node           # Link previous node to new node
        new_node['next'] = next_leader      # Link new node to what was at target index
        self.length +=1
        return self.print_list()            # Return updated node values

    def get_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index :
            current_node = current_node['next'] # Move to the next node
            counter+=1
        return current_node                     # Return the node at requested index

    def __str__(self):
        return str(self.__dict__)

    def print_list(self):
        arr = []                                # Array to collect values
        current_node = self.head                # Start from head
        while (current_node['next'] != None):   # Traverse until the last node
            arr.append(current_node['value'])
            current_node = current_node['next']
        arr.append(self.tail['value'])          # Add the final node's value
        return arr

    def delete(self, index):
        leader = self.get_index(index - 1)      # Find the node right before the one we want to
        deleting_node = leader['next']          # The node to remove
        leader['next'] = deleting_node['next']  # Point the previous node to the next-next
        self.length -= 1
        return self.print_list()

    def help(self):
        print("\n📘 Available Methods in My Dictionary-Based Linked List")
        print("----------------------------------------------------")
        print("append(data)       --> Add element to the end of the list")
        print("prepend(data)      --> Add element to the beginning of the list")
        print("insert(index, val) --> Insert value at specific index; if index >= length, append to end")
        print("delete(index)      --> Delete node at given index")
        print("get_index(index)   --> Return the node (dictionary) at the given index")
        print("print_list()       --> Return list of all values in order")
        print("help()             --> Display this help message")
        print("----------------------------------------------------\n")


ll = LinkedList(29)
ll.help()
print(ll.print_list())
ll.append(1)
ll.prepend(12)
print(ll.print_list())
ll.insert(2,20)
print(ll.print_list())
print(ll.get_index(3))
print(ll.get_index(1))
ll.delete(2)
print(ll.print_list())
print(ll.insert(10,20))

'''
This is not the classic Linked List. Nodes in this are dictionaries instead of objects of Node Class. 
Instead of relying on dot syntax of node attribute to access node class, we use dictionary access method here.
Hence, Not very object oriented. So not recommended.
But structure wise, methods wise and fundamentally it is a Linked List. 
I will be building an object oriented linked list in next file in same directory.
'''