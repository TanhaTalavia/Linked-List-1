# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n) :

        if head is None:
            return head

        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = dummy

        counter = 0

        while counter <= n:
            fast = fast.next
            counter += 1
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next