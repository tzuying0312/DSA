class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
        
'''
seq[start:end:step]
ex: 
range(10)[::2]
ans:[0, 2, 4, 6, 8]
'''
