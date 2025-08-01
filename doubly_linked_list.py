class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.prev = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            self.prev = self.tail
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
            self.head.prev = new_node
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
        #   Method 3
        else:
            leader = self.traversetoindex(index - 1)
            holder = leader.next
            leader.next = new_node
            new_node.next = holder
            new_node.prev = leader
            holder.prev = new_node
            self.length += 1

        ''' - Method 1
        while i <= self.length:
            if i == index - 1:
                new_node.next, temp.next = temp.next, new_node
                self.length += 1
                break # To break the while loop and exit.
            temp = temp.next
            i += 1
        '''
        '''
        # Method 2
        while i < index - 1:
            temp = temp.next
            i += 1

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        '''

    def traversetoindex(self, index):
        curr_node = self.head
        i = 0
        while i != index:
            curr_node = curr_node.next
            i += 1
        return curr_node

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

        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return

        # Method 3
        leader = self.traversetoindex(index - 1)
        unwanted_node = leader.next
        holder = unwanted_node.next
        leader.next = holder
        holder.prev = leader
        self.length -= 1

        ''' Method 1
        while i <= self.length:
            if i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                break
            i += 1
            temp = temp.next
        '''
        ''' Method 2
        while i < index - 1:
            temp = temp.next
            i += 1
        temp.next = temp.next.next
        if index == self.length - 1:
            self.tail = temp  # ✅ Update tail if last node was deleted
        self.length -= 1
        '''

    def printl(self):
        arr = []
        temp = self.head
        while temp is not None:
            arr.append(temp.value)
            temp = temp.next
        return f"{arr} | Length = {str(self.length)}"


d = DoublyLinkedList()
d.append(10)
d.append(5)
d.append(6)
d.prepend(1)
d.insert(2,22)
d.delete(3)
print(d.printl())