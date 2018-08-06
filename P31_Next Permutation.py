class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums); i = l - 1
        if l <= 1:
            return

        while(i > 0 and nums[i] <= nums[i - 1]):
            i -= 1
        if i == 0:
            for x in range(l//2):
                nums[x], nums[l-x-1] = nums[l-x-1], nums[x]
            return
        if i == l - 1:
            nums[i], nums[i-1] = nums[i-1], nums[i]
            return
        j = i+1
        while(j < len(nums) and nums[j] > nums[i-1]):
            j += 1
        j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        for x in range(0, (l-i)//2):
            nums[i+x], nums[l-x-1] = nums[l-x-1], nums[i+x]
        return


x = Solution()
print(x.nextPermutation([1]))
print(x.nextPermutation([1,2,3,4]))
print(x.nextPermutation([4,3,2,1]))
print(x.nextPermutation([5,1,1]))
print(x.nextPermutation([1,5,1]))
print(x.nextPermutation([1,2,5,4,3]))
print(x.nextPermutation([1,3,5,4,2,1]))
