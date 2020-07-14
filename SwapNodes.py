#Given a linked list, swap every two adjacent nodes and return its head.
#You may not modify the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        current = head
        while current != None and current.next != None:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next
        
        return head
        
