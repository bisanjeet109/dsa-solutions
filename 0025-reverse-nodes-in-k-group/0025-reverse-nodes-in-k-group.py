class Solution:
    def reverseKGroup(self, head, k):
        # Check whether k nodes are available
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        # Reverse k nodes
        prev = None
        curr = head

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # head is now the last node of this group
        head.next = self.reverseKGroup(curr, k)

        return prev