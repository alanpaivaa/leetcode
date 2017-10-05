class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """

        current_a = headA
        current_b = headB

        count_a = 0
        count_b = 0

        while current_a != None :
            count_a += 1
            current_a = current_a.next

        while current_b != None :
            count_b += 1
            current_b = current_b.next

        current_a = headA
        current_b = headB

        while count_a > count_b:
            current_a = current_a.next
            count_a -= 1

        while count_b > count_a:
            current_b = current_b.next
            count_b -= 1

        while current_a != current_b:
            current_a = current_a.next
            current_b = current_b.next

        return current_a