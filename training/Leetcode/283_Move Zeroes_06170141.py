class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            while (nums[i] == 0):
                del nums[i]
                nums.insert(len(nums), 0)
                if nums[i:len(nums)] == [0]*len(nums[i:len(nums)]):
                    break
