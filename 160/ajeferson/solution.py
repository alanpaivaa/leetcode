class Solution(object):

    def sum(self, head):
        s = 0
        while(head):
            s += head.val
            head = head.next
        return s

    def getIntersectionNode(self, a, b):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        sa = self.sum(a)
        sb = self.sum(b)
        while(a and b):
            if sa == sb and a == b:
                return a
            elif sa > sb:
                sa -= a.val
                a = a.next
            else:
                sb -= b.val
                b = b.next
