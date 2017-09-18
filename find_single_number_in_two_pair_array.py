class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        j = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[j] == nums[j+1]:
                j = j+2
            else:
                return nums[j]
            if j >= len(nums) - 2:
                return nums[len(nums) - 1]
                break
