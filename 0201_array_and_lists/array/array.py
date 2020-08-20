class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        left = 0

        for i, v in enumerate(nums):
            if left == s - left - v:
                return i

            left += v

        return -1


nums = [1, 7, 3, 6, 5, 6]
print(Solution().pivotIndex(nums=nums))
