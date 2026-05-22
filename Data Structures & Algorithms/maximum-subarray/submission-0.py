class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        s, max_sum = 0, float('-inf')
        for num in nums:
            s += num
            max_sum = max(s, max_sum)

            if s<0:
                s = 0
        return max_sum
        