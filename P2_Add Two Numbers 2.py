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
        re = l

        carry = 0
        while(l1 != None or l2 != None ):
            x = l1.val if l1!=None else 0
            y = l2.val if l2!=None else 0
            sum = x + y + carry
            l.next = ListNode(sum % 10)
            carry =(int) (sum / 10)
            l1 = l1.next if l1!= None else None
            l2 = l2.next if l2!= None else None
            l = l.next

        if carry == 1:
            l.next =  ListNode(1)

        return re.next

# Test
a=Solution()

l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
#l6 = ListNode(7)
l4.next = l5
#l5.next = l6

l7 = None

result = a.addTwoNumbers(l1,l4)

while(result != None):
    print(result.val)
    result = result.next