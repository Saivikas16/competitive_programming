# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l=[]
        while(head):
            l.append(head.val)
            head=head.next
        dec=0
        length=0
        while l:
            dec=dec+2**length*l.pop()
            length+=1
        return dec
