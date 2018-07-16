# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while(head != None and head.val == val):
            head = head.next
        prev = head

        while(head!=None and head.next != None):
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return prev


a = Solution()
ll = None
l1 = ListNode(1)
l2 = ListNode(3)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

l = a.removeElements(l1,2)
while (l!= None):
    print(l.val)
    l = l.next


