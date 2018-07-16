class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0; right = sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1

x = Solution()
print(x.pivotIndex([1, 7, 3, 6, 5, 6]))
print(x.pivotIndex([1, 2, 3]))
