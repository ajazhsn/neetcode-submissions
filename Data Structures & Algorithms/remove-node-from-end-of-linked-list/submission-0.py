class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        count = 0

        while curr.next:
            count += 1
            curr = curr.next

        key = count - n
        curr = dummy
        counter = 0

        while counter != key:
            counter += 1
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next