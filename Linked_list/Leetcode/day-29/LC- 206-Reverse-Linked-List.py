# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev_node= None
        curr=head
        while curr is not None:
            next_node=curr.next
            curr.next= prev_node
            prev_node= curr
            curr= next_node
        return prev_node
