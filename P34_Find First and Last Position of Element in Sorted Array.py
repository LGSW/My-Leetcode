class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        re = False
        left = 0; right = len(nums)-1
        while(left <= right):
            mid = (left+ right)//2
            if nums[mid] == target:
                re = True
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if not re:
            return [-1, -1]

        left1 = left; right1 = mid
        while(left1 <= right1):
            mid1 = (left1 + right1) // 2
            if nums[mid1] >= target:
                right1 = mid1- 1
            else:
                left1 = mid1 + 1

        left2 = mid; right2 = right
        while (left2 <= right2):
            mid2 = (left2 + right2) // 2
            if nums[mid2] <= target:
                left2 = mid2 + 1
            else:
                right2 = mid2 - 1

        return [left1, right2]

x = Solution()
print(x.searchRange([5,7,7,8,8,10], 6))
print(x.searchRange([5,7,7,8,8,10], 8))
print(x.searchRange([5,7,7,8,8,8,10], 8))
print(x.searchRange([1,2,2,2,2,2,2], 2))
print(x.searchRange([2,2,2,2,2,2,6], 2))
print(x.searchRange([2,2,2,2,2,2,2], 2))

