class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find middle using slow/fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        curr = slow.next
        slow.next = None  # cut the list in half
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: interleave
        l1, l2 = head, prev
        while l1.next and l2:
            temp = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp
            l1 = temp
            l2 = temp2