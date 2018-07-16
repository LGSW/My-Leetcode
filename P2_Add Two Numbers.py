# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1


        l = ListNode(0)
        l.next = l1

        flg = 0
        while(l1!= None and l2!= None):
            sum = l1.val + l2.val + flg
            l1.val = sum % 10
            flg =(int) (sum / 10)
            l1 = l1.next
            l2 = l2.next

        if l2 != None:
            l1 = l2

        while l1 != None:
            sum = l1.val + flg
            l1.val = sum % 10
            flg = (int)(sum / 10)
            l1 = l1.next

        if flg == 1:
            l1= ListNode(1)

        return l.next

# Test
a=Solution()
l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(6)
l4.next = l5
l5.next = l6

l7 = None

result = Solution().addTwoNumbers(l1,l4)

while(result != None):
    print(result.val)
    result = result.next