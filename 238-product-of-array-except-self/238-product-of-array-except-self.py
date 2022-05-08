class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        p = 1
        for idx in range(len(nums)):
            answer.append(p)
            p *= nums[idx]

        p = 1
        for idx in range(len(nums) - 1, 0 - 1, -1):
            answer[idx] *= p
            p *= nums[idx]

        return answer