class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for n in range(len(nums)):
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perms.append(perm[:i] + [nums[n]] + perm[i:])
                    print(n, i, perm, new_perms)
            perms = new_perms

        return perms

x = Solution()
print(x.permute([1,2]))
print(x.permute([1,2,3]))
print(x.permute([1,2,3,4]))


