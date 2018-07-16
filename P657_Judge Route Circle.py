class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')

    def judgeCircle1(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        direc = [0, 0]
        for i in moves:
            if i == 'L':
                direc[0] += 1
            elif i == 'R':
                direc[0] -= 1
            elif i == 'U':
                direc[1] += 1
            elif i == 'D':
                direc[1] -= 1
        return direc[0]==0 and direc[1]==0

x = Solution()
print(x.judgeCircle('UD'))
print(x.judgeCircle('LR'))
print(x.judgeCircle('LL'))
print(x.judgeCircle("LDRRLRUULR"))
