class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = []
        sorted_nums = sorted(nums, reverse=True)
        for n in nums:
            rank = sorted_nums.index(n)
            if rank == 0:
                ans.append('Gold Medal')
            elif rank == 1:
                ans.append('Silver Medal')
            elif rank == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(rank + 1))
        return ans

x = Solution()
print(x.findRelativeRanks([5,4,3,2,1]))
print(x.findRelativeRanks([3,2,5,4,3,2,1,4]))