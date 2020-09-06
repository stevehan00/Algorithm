class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = 0
        while s < len(nums) - 1:
            if nums[s] == nums[s+1]:
                nums.pop(s)
            else:
                s += 1
        return len(nums)