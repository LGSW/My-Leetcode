class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                res.append(S)
            if left < n:
                backtrack(S + '(' , left + 1, right)
            if left > right:
                backtrack(S + ')', left, right + 1)

        res = []
        backtrack()
        return res

    def generateParenthesis2(self, n): ################
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
        return ans

    def generateParenthesis3(self, n):
        def generate(A = []):
            if len(A) == 2 * n:
                if valid(A):
                    res.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            cnt = 0
            for c in A:
                if c == '(': cnt += 1
                else: cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0

        res = []
        generate()
        return res



x = Solution()
print(x.generateParenthesis2(1))
print(x.generateParenthesis2(2))
print(x.generateParenthesis2(3))
print(x.generateParenthesis2(4))
