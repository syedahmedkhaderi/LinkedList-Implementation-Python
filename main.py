class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index <= 0:
            self.prepend(value)
            return
        if index >= self.length:
            self.append(value)
            return
        i = 0
        temp = self.head
        ''' - Method 1
        while i <= self.length:
            if i == index - 1:
                new_node.next, temp.next = temp.next, new_node
                self.length += 1
                break # To break the while loop and exit.
            temp = temp.next
            i += 1
        '''
        # Method 2
        while i < index - 1:
            temp = temp.next
            i += 1

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    def delete(self, index):
        temp = self.head
        i = 0
        if index < 0 or index >= self.length:
            print("Entered wrong index")
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            if self.length == 0:
                self.tail = None  # Handle empty list
            return

        while i <= self.length:
            if i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                break
            i += 1
            temp = temp.next

        ''' Method 2
        while i < index - 1:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        if index == self.length - 1:
            self.tail = temp  # ✅ Update tail if last node was deleted
        self.length -= 1
        '''

    def reverse(self):
        pass
    def printl(self):
        arr = []
        temp = self.head
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        return f"{arr} | Length = {str(self.length)}"

ll = LinkedList()
ll.append(5)
ll.prepend(6)
ll.append(7)
ll.insert(5,8)
ll.insert(1, 6.5)
ll.insert(0,5.5)
ll.delete(0)
ll.delete(10)
ll.delete(1)
print(ll.printl())


