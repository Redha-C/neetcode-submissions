class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_length = 2 * n
        ans = [0] * ans_length

        for i, num in enumerate(nums):
            ans[i] = ans[i + n] = num

        return ans
    