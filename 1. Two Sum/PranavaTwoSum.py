class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = set(nums)

        for i in range(len(nums)):
            if ((target - nums[i]) in numbers):
                temp = nums.index(target - nums[i])
                if (temp != i):
                    return [i, nums.index(target - nums[i])]
