class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms =[[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    if (perm[:i] + [n] + perm[i:]) not in new_perms:
                        new_perms.append(perm[:i] + [n] + perm[i:])
            perms = new_perms

        return perms

x = Solution()
print(x.permuteUnique([1]))
print(x.permuteUnique([1,1]))
print(x.permuteUnique([1,2]))
print(x.permuteUnique([2,2,2]))
print(x.permuteUnique([1,2,2,3]))
print(x.permuteUnique([1,2,3,3]))

