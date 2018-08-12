class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, index, target, path, res):
            if target < 0:
                return
            if target == 0:
                if path not in res:
                    res.append(path)
                return
            for i in range(index , len(candidates)):
                dfs(candidates, i+1, target - candidates[i], path + [candidates[i]], res)

        res = []
        candidates.sort()
        dfs(candidates, 0, target, [], res)
        return res

    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        if not target:
            result.append(path)
            return

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            if nums[i] > target:
                break
            self.combine_sum_2(nums, i + 1, path + [nums[i]],result, target - nums[i])

x = Solution()
print(x.combinationSum2([1,2,3],4))
print(x.combinationSum2([2,3,5],8))
print(x.combinationSum2([10,1,2,7,6,1,5],8))