class LinkedList:
    def __init__(self, value):
        self.head = {
            'value' : value ,
            'next' : None
        }
        self.tail = self.head
        self.length = 1
        print("Hi, This is My Dictionary Based Linked List. Use Method 'help()' for listing all the methods")

    def append(self, data):
        new_node = {
            "value" : data ,
            "next" : None
        }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, data):
        new_node = {
            "value": data,
            "next": None
        }
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1
        return self

    def insert(self, index, value):
        new_node = {
            "value": value,
            "next": None
        }

        if index >= self.length:
            self.append(value)
            return self.print_list()

        leader = self.get_index(index - 1)
        next_leader = leader['next']
        leader['next'] = new_node
        new_node['next'] = next_leader
        self.length +=1
        return self.print_list()

    def get_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index :
            current_node = current_node['next']
            counter+=1
        return current_node

    def __str__(self):
        return str(self.__dict__)

    def print_list(self):
        arr = []
        current_node = self.head
        while (current_node['next'] != None):
            arr.append(current_node['value'])
            current_node = current_node['next']
        arr.append(self.tail['value'])
        return arr

    def delete(self, index):
        leader = self.get_index(index - 1)
        deleting_node = leader['next']
        leader['next'] = deleting_node['next']
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


ll = LinkedList(10)
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

