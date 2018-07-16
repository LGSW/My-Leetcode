class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low = 0; high = len(letters)-1
        while(low < high):
            mid = low + (high - low) // 2
            if (letters[mid] <= target):
                low = mid + 1
            else:
                high = mid
        return letters[0] if target >= letters[low] else letters[low]

    def nextGreatestLetter1(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

x = Solution()
print(x.nextGreatestLetter( ["c", "f", "j"], "a"))
print(x.nextGreatestLetter( ["c", "f", "j"], "d"))
print(x.nextGreatestLetter( ["c", "f", "j"], "j"))