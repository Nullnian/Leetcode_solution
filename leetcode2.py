# Question 2:
    # You are given two non-empty linked lists representing two non-negative integers. 
    # The digits are stored in reverse order, and each of their nodes contains a single digit. 
    # Add the two numbers and return the sum as a linked list.
    # You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         

# The leetcode solution
class solution:
    def addTwoNumbers(self, l1, l2):
        re = temp = ListNode(None)    #create two linked lists
        add = 0
        while l1 or l2 or add:    # when l1 have node or l2 have node
            add += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            temp.next = ListNode(add % 10)  
            add //= 10
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return re.next



