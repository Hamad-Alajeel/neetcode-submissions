# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        elif head.next == None:
            return head
        else:
            predecessor = None
            cur = head
            successor = head.next
            while successor:
                cur.next = predecessor
                predecessor = cur
                cur = successor
                successor = successor.next

            cur.next = predecessor

            return cur
        