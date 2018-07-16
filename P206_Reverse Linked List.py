# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = None; nex = None
        while(head != None):
            nex = head.next
            head.next = cur
            cur = head
            head = nex

        return cur

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4

a = Solution()
new_l = a.reverseList(l1)
while(new_l != None):
    print(new_l.val)
    new_l = new_l.next