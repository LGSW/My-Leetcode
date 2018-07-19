# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        l = 1; tail = head
        while(tail.next != None):
            tail = tail.next
            l += 1
        k = k % l
        if k == 0:
            return head
        h = head
        for i in range(l - k - 1):
            h = h.next
        st = h.next
        tail.next = head
        h.next = None
        return st

x = Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
h = x.rotateRight(a1,2)
while(h):
    print(h.val)
    h = h.next