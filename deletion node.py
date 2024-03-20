Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Definition for singly-linked list.
... # class ListNode:
... #     def __init__(self, x):
... #         self.val = x
... #         self.next = None
... 
... class Solution:
...     def deleteNode(self, node):
...         """
...         :type node: ListNode
...         :rtype: void Do not return anything, modify node in-place instead.
...         """
...         node.val=node.next.val
