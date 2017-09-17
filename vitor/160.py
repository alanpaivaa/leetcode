# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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


        '''
        while nextNodeA != None:
            while nextNodeB != None:
                if nextNodeA is nextNodeB:
                    return nextNodeA
                nextNodeB = nextNodeB.next
            nextNodeA = nextNodeA.next
            nextNodeB = headB
        return None




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
