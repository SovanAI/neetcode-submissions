class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left , right = 0 , 0
        ans = []
        sum = 0
        for left in range(0, len(nums) - 1):
            for right in range(left + 1, len(nums)):
                sum = nums[left] + nums[right]
                if target == sum :
                    ans.append(left)
                    ans.append(right)
                    return ans
        return ans