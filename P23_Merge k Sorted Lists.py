# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue

class Solution(object):
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        count = 0
        for node in lists:
            if node: q.put((node.val, count, node))
            count += 1
        while q.qsize() > 0:
            curr.next = q.get()[2]
            curr = curr.next
            if curr.next: q.put((curr.next.val, count, curr.next))
            count += 1
        return dummy.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        count = 0
        for node in lists:
            while node:
                q.put((node.val, count, node))
                count += 1; node = node.next
        while q.qsize() > 0:
            curr.next = q.get()[2]
            curr = curr.next
        return dummy.next


a1 = ListNode(1); a2 = ListNode(4); a3 = ListNode(5)
a1.next = a2; a2.next = a3
b1 = ListNode(1); b2 = ListNode(3); b3 = ListNode(4)
b1.next = b2; b2.next = b3
c1 = ListNode(2); c2 = ListNode(6)
c1.next = c2
x = Solution()

result = (x.mergeKLists([a1,b1,c1]))
while(result):
    print(result.val)
    result = result.next