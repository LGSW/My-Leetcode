class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result =[0, 0]; s = 0
        dic = dict()
        for i in range(len(nums)):
            s = s ^ nums[i] ^ (i+1)
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] = 2
                result[0] = nums[i]
        result[1] = result[0] ^ s
        return result

x = Solution()
print(x.findErrorNums([1,2,2,4]))