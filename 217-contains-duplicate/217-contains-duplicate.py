class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for idx, num in enumerate(nums):
            if idx == len(nums) - 1:
                break
            if num == nums[idx+1]:
                return True
        return False