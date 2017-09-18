class Solution(object):
    def __init__(self):
        pass
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        while n:
            if n % 2 == 1:
                c += 1
            n = n >> 1
        if c == 1:
            return True
        else:
            return False

my_solution = Solution()
my_solution.isPowerOfTwo(-16)
