class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.lst) == 0:
            self.min_v = x
        self.lst.append(x - self.min_v)
        if x < self.min_v:
            self.min_v = x

    def pop(self):
        """
        :rtype: void
        """
        v = self.lst.pop()
        if v < 0:
            item_to_pop = self.min_v
            prev_min_v = item_to_pop - v
            self.min_v = prev_min_v
            return item_to_pop
        else:
            return v + self.min_v


    def top(self):
        """
        :rtype: int
        """
        v = self.lst[-1]

        if v < 0:
            item_to_pop = self.min_v
            return item_to_pop
        else:
            return v + self.min_v


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_v


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

