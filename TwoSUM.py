'''
Hash tables
O(N) time, O(N) space
'''

def twoSum(nums, target):
    if not nums or len(nums) < 2:
        return []
    seen = {}
    for i in range(len(nums)):
        numNeeded = target - nums[i]
        if numNeeded in seen:
            return [i, seen[numNeeded]] # reurn the index of the pairs
        else:
            seen[nums[i]] = i

print(twoSum([1,2,3,4,7,8,9], 7))