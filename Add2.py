#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num = 0
        deg = 0
        l = []
        while l1 != None or l2 != None:
            print(num, deg)
            if l1 == None:
                num += l2.val * (10 ** deg)
                print("1",num, deg, (num / (10 ** deg)) % 10)
                l2 = l2.next
            elif l2 == None:
                num += l1.val * (10 ** deg)
                print("2",num, deg, (num / (10 ** deg)) % 10)
                l1 = l1.next
            else :
                num += (l2.val + l1.val) * (10 ** deg)
                print("3",num, deg, (num / (10 ** deg)) % 10)
                l1 = l1.next
                l2 = l2.next
            deg += 1
        while num > 0:
            l.append(ListNode(val = num % 10))
            num /= 10
        if len(l) == 0:
            return ListNode()
        for i in range(0,(len(l)-1)):
            print(i)
            l[i].next = l[i+1]
        return l[0]
