class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortnums = nums.copy()
        sortnums.sort()
        k1 = 0; k2 = 0
        for (i,j) in zip(nums, sortnums):
            if i != j:
                break
            k1 += 1
        if k1 == len(nums):
            return 0
        for (i,j) in zip(nums[::-1], sortnums[::-1]):
            if i != j:
                break
            k2 += 1
        return len(nums) -k1 - k2

x = Solution()
print(x.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(x.findUnsortedSubarray([1, 2, 3, 4]))