class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}
        for i, j in enumerate(nums):
            complement = target - j
            if complement in nums_dict:
                return [nums_dict[complement], i]
            nums_dict[j] = i


nums = [3, 2, 4]
target = 6
use = Solution()
data = use.twoSum(nums, target)
print(data)
