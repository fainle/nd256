
class Solution:
    def removeDuplicates(self, nums) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return 0

        return len(nums)


s = Solution()
assert s.removeDuplicates([1, 2, 3, 4]) == 4
assert s.removeDuplicates([1, 1, 1, 4]) == 2
assert s.removeDuplicates([1, 1, 1, 1]) == 0