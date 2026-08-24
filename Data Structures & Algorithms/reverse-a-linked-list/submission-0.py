# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            temp = curr.next #keep track of next node
            curr.next = prev #reassign next of current node to reverse point
            prev = curr #assign prev to be current node that was reversed
            curr = temp #assign cur to be temp (next node)
        return prev #prev is new head of list after while loop breaks        