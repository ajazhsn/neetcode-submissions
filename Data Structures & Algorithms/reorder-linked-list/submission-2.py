class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1

        print(count//2)

        c = 0
        lt = None
        rt = head 
        while rt:
            while c < count//2:
                rt = rt.next
                c += 1
            else:
                break

        lt = rt.next
        rt.next = None

        curr = lt
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        new_head = prev

        while prev:
            prev = prev.next

        l1 = head
        l2 = new_head

        while l1.next and l2:
            temp = l1.next
            temp2 = l2.next 
            l1.next = l2
            l2.next = temp
            l1 = temp
            l2 = temp2

        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next

        print(result)