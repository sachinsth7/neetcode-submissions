# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        temp = None
        while second:
            next_node = second.next
            second.next = temp
            temp = second
            second = next_node
        first = head
        second = temp
        while second:
            t1 = second.next
            t2 = first.next
            first.next = second
            second.next = t2
            first = t2
            second = t1

