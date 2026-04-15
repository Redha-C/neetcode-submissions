from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = defaultdict(int)
        indices = []

        for index, num in enumerate(nums):
            diff = target - num 

            if diff in diffMap:
                return [diffMap[diff], index]
            
            diffMap[num] = index
