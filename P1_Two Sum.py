class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indx = {}
        for i in range(len(nums)):
            if nums[i] not in indx:
                indx[target - nums[i] ] = i
            else:
                return(indx[nums[i]], i)


a = Solution()
result = a.twoSum([1,2,5,7], 12)
print(result)
