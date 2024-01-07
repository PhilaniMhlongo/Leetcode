"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://leetcode.com/problems/add-two-numbers/

"""

from collections import deque
from typing import Self

# lit=deque()
# lit.append('A')
# lit.append('B')
# lit.appendleft('C')


# print(lit)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        list1=deque()
        list2=deque()
        for i in l1:
            list1.appendleft(i)
        for k in l2:
            list2.appendleft(k)
        
       
               
        #print(list2)
        #l3=l1[::-1]
        #l4=l2[::-1]
        
        #l5=" ".join(l3)
        #l6=" ".join(l4)
        #l7=int(l5)
        #l8=int(l6)
        
        
        # Definition for singly-linked list.
        
    if __name__=="__main__":
        l1 = [2,4,3]
        l2 = [5,6,4]
        addTwoNumbers(Self,l1,l2)