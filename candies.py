class Solution(object):
    def __init__(self):
        pass
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        my_dictionary = {}
        for i in range(len(candies)):
            my_dictionary[candies[i]] = 1 + my_dictionary.get(candies[i] , 0)
        count = 0
        for i in my_dictionary:
            if my_dictionary[i] >= 1 :
                count = count + 1
        return count if count < len(candies)/2 else len(candies)/2
new_solution = Solution()
new_solution.distributeCandies([0,0,14,0,10,0,0,0])
