class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        places = [p for p in path.split("/") if p != "." and p != ""]
        print(places)
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)


x = Solution()
print(x.simplifyPath("/a/./b/../../c/"))
print(x.simplifyPath("/home/"))
print(x.simplifyPath("/home//foo/"))