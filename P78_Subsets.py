class Solution(object):
    # DFS recursively
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    # Bit Manipulation
    def subsets1(self, nums): 
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    # iteratively
    def subsets2(self, nums):
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res

x = Solution()
print(x.subsets([1,2]))
print(x.subsets([1,2,3]))
print(x.subsets([1,2,3,4]))
