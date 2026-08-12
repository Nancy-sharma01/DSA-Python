"""
Problem:
Insert a node at the beginning of a singly linked list.
Platform: HackerRank
"""

def insertNodeAtHead(head, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = head
    return new_nodes