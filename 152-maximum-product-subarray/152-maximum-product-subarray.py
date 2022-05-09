class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxValue = big = small = nums[0]
        for i in range(len(nums)):
            if i == 0:
                continue

            x = max(nums[i], nums[i]*big, nums[i]*small)
            y = min(nums[i], nums[i]*big, nums[i]*small)
            big = x
            small = y
            maxValue = max(maxValue, big)

        return maxValue