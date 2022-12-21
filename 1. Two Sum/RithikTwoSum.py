#If it was a sorted array, could use the 2 pointer approach
#hashmap is O(n) and space O(n)

def twoSum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
        difference = target - num
        if difference in hashmap:
            return hashmap[difference], index
        hashmap[num] = index


nums = [3, 2, 4]
target = 6
twoSum(nums, target)
