# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        while temp.next!=None:
            data=gcd(temp.val,temp.next.val)
            node=ListNode(data)
            node.next=temp.next
            temp.next=node
            temp=temp.next.next
        return head
            
