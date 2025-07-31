from sqlite3 import DataError


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = {
            'value' : value ,
            'next' : None
        }
        self.tail = self.head
        self.length = 1

    def append(self, data):
        newnode = {
            "value" : data ,
            "next" : None
        }
        self.tail['next'] = newnode
        self.tail = newnode
        self.length += 1
        return self

    def prepend(self, data):
        newnode = {
            "value": data,
            "next": None
        }
        newnode['next'] = self.head
        self.head = newnode
        self.length += 1
        return self

    def insert(self, index, value):
        newnode = {
            "value": value,
            "next": None
        }
        leader = self.get_index(index - 1)
        next_leader = leader['next']
        leader['next'] = newnode
        newnode['next'] = next_leader
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

l = LinkedList(10)
print(l)
l.append(15)
l.append(20)
print(l)
l.prepend(5)

l.print_list()

print("This is getting Index Method: " + str(l.get_index(3)))
l.insert(1,8)

print(l.print_list())
print(l.delete(3))