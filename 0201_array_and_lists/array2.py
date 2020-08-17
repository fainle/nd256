class Solution(object):
    def searchInsert(self, nums, target):
        tem_index = 0

        for i, v in enumerate(nums):
            if target == v:
                return i

            if target > v:
                tem_index = i + 1

        return tem_index


nums = [1, 3, 5, 6]
s = Solution()

assert s.searchInsert(nums=nums, target=5) == 2
assert s.searchInsert(nums=nums, target=2) == 1
assert s.searchInsert(nums=nums, target=7) == 4
assert s.searchInsert(nums=nums, target=0) == 0
