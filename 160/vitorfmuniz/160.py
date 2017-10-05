# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#my solution 496 ms is using the hash table is not the best solution
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        nodes_dict = {}
        nextNodeA = headA
        nextNodeB = headB

        while nextNodeA != None:
            nodes_dict[nextNodeA] = nextNodeA
            nextNodeA = nextNodeA.next

        while nextNodeB != None:
            try :
                return nodes_dict[nextNodeB]
            except KeyError:
                nodes_dict[nextNodeB] = nextNodeB
            nextNodeB = nextNodeB.next
        return None

''' #solution with a set (implemented with hashtable) instead a dict, because the keys doesn't matter
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        c=set()
        while headA:
            c.add(headA)
            headA=headA.next
        while headB:
            if headB in c:
                return headB
            else:
                headB=headB.next
'''

''' #solution with two pointers is the best, because the memory is always O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa
'''

#Test Solution
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)

headA = ListNode(0)
headB = ListNode(0)

headA.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

headB.next = node6
node6.next = node7
node7.next = node8
node8.next = node3

print(Solution().getIntersectionNode(headA,headB).val)

'''
