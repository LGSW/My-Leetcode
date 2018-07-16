class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        score = []
        for i in range(len(ops)):
            if ops[i] == '+':
                s = score[-1] + score[-2]
                score.append(s)
            elif ops[i] == 'C':
                score.pop()
            elif ops[i] == 'D':
                s = 2 * score[-1]
                score.append(s)
            else:
                s = int(ops[i])
                score.append(s)
        return sum(score)

x = Solution()
print(x.calPoints( ["5","2","C","D","+"]))
print(x.calPoints( ["5","-2","4","C","D","9","+","+"]))