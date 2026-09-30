class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for left in range(0, len(nums) - 1):
            if nums[left] == nums[left + 1]:
                return True
        return False
