class Solution:
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        i = 0
        while i < len(nums):
            cur = 0
            while i < len(nums) and nums[i] == 1:
                i += 1
                cur += 1
            i += 1
            ans = max(ans, cur)
        return ans

x = Solution()
print(x.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(x.findMaxConsecutiveOnes([1,0,1,1]))
print(x.findMaxConsecutiveOnes([0,1,0,0,1,1,1,0,1,1]))