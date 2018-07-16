class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rl = len(nums)
        cl = len(nums[0])
        if rl * cl != r * c:
            return nums
        newnums = []
        for i in range(len(nums)):
            newnums += nums[i]
        result =[]
        for i in range(0,r*c,c):
            result.append(newnums[i:i+c])
        return result

x = Solution()
print(x.matrixReshape([[1,2],[3,4]],1,4))
print(x.matrixReshape([[1,2],[3,4],[5,6]],2,3))
print(x.matrixReshape([[1,2],[3,4],[5,6]],3,3))

