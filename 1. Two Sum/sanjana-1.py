class Solution:
    
    # Brute Force
    # Runtime O(n^2), Space O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            pivot = nums[i]
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[j] + pivot == target:
                    return [i, j]
        return []

    # One-Pass Hash Map 
    # Runtime O(n), Space O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        seen = {}
        for i, item in enumerate(nums):
            complement = target-item
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[item] = i
        
        return []