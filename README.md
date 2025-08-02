# Linked List Implementations in Python

My first comprehensive learning project demonstrating different types of **linked lists** using Python — featuring various implementations:

- Singly Linked List  
- Doubly Linked List  
- Circular Linked List  
- Reversal Operation (Singly)  
- Dictionary-Based Linked List (non-classic, more intuitive)

## What’s Inside

| Data Structure        | Features                                      |
|-----------------------|-----------------------------------------------|
| Singly Linked List    | Append, Prepend, Insert, Delete, Reverse      |
| Doubly Linked List    | Bidirectional traversal, Append, Delete       |
| Circular Linked List  | Last node points to head                      |
| Dictionary-Based List | Simplified syntax using dicts and key access  |

## Folder Structure

```
linkedlist-python/
├── singly_linked_list.py
├── doubly_linked_list.py
├── circular_linked_list.py
├── dict_linked_list.py
├── README.md
```

## Singly Linked List

A basic implementation using `Node` and `LinkedList` classes.

Implements:

- `append()`
- `prepend()`
- `insert()`
- `delete()`
- `reverse()`
- `printl()`

### Reverse Method

Reverses the linked list **in-place** (without using extra space):

```python
def reverse(self):
    prev, curr = None, self.head
    self.tail = self.head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    self.head = prev
```

## Doubly Linked List

Supports forward and backward traversal.

- Maintains both `next` and `prev` pointers for each node
- Efficient traversal from both ends

## Circular Linked List

A type of linked list where the last node points back to the `head`.

- Useful for round-robin scheduling
- Optionally both singly and doubly circular variations

## Dictionary-Based Linked List

A more Pythonic and beginner-friendly variation.

```python
node1 = {'value': 10, 'next': None}
node2 = {'value': 20, 'next': None}

node1['next'] = node2
```

- No object-oriented classes or methods required
- All nodes are simple Python dictionaries
- Easier to debug and visualize

Great for beginners  
No need for custom Node class


## Concepts Covered

- Singly/Double/Circular linked lists
- Object-oriented vs dictionary-based data structures
- Pointer manipulation and reversal logic
- Edge case handling and dynamic memory modeling


## Requirements

- Python 3.7+  
- No external libraries required  
- Runs directly on the CLI or any Python interpreter

## ▶ How to Run

```bash
python3 SLL_Notes.py.py
python3 doubly_linked_list.py
python3 circular_linked_list.py
python3 dict_linked_list.py
```

## 📝 License

This project is licensed under the **MIT License** — free to use, modify, and share.

