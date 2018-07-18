# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        for i in sorted(intervals, key=lambda i: i.start):
            if result and i.start <= result[-1].end:
                result[-1].end = max(result[-1].end, i.end)
            else:
                result += i,
        return result

x = Solution()
a = Interval(1,3)

result1 = x.merge([Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18)])
for i in result1:
    print(i.start, i.end)
print()
result1 = x.merge([Interval(1,3),Interval(0,6),Interval(8,19),Interval(7,18)])
for i in result1:
    print(i.start, i.end)
