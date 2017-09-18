class Solution(object):
    def __init(self):
        pass
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        last = len(nums)
        first = 0
        not_found = True
        while not_found:
            middle = int((last + first)/2)
            if first == last:
                return first
            elif first + 1 == last and target < nums[first]:
                return first
            elif first + 1 == last and target > nums[first]:
                return first + 1

            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                first = middle
            elif target < nums[middle]:
                last = middle

my_solution = Solution()
print my_solution.searchInsert([1],0)
