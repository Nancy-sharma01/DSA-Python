"""
Problem:
Print the data of each node in a singly linked list.
Platform: HackerRank
"""

def printLinkedList(head):
    current = head

    while current:
        print(current.data)
        current = current.next