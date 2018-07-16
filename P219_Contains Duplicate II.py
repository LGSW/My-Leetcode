class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        h = {}
        for i, num in enumerate(nums):
            if num in h and i - h[num] <= k:
                return True
            h[num] = i
        return False


a = Solution()
print(a.containsNearbyDuplicate([1,2,3,1], 3))