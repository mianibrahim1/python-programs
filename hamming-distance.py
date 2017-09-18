class Solution(object):
    def __init__(self):
        pass
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        while n != 0:
            if n % 2 == 1:
                r += 1
            n = n >> 1
            print n
        return r

my_solution = Solution()
my_solution.hammingWeight(2)
