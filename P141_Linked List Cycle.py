# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None or head.next == None:
            return False

        t1 = head
        t2 = head.next

        iter = 0
        while(t1 != t2 and t1.next != None and t2.next != None and t2.next.next != None):
            t1 = t1.next
            t2 = t2.next.next

        if t1 != None and t2 != None and t1 == t2 :
            return True

        return False

# Test
# ------------------------------------------------------------------

l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2

test = Solution()
print(test.hasCycle(l1))