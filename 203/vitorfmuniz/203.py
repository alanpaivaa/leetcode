# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# my solution
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        nodeA = head

        if head is None:
            return head

        while nodeA.next:
            if nodeA.next.val is val:
                nodeA.next = nodeA.next.next
            else:
                nodeA = nodeA.next

        if head.val is val:
            head = head.next

        return head

''' best solution
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val: # find the new head if the head is the value
            head = head.next
        p = head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head
'''

node1 = ListNode(5)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)

headA = ListNode(5)

headA.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

next = Solution().removeElements(headA,5)
'''
 0 1 2 3 5 4 5
'''

#next = headA
while next:
    print(next.val)
    next = next.next
