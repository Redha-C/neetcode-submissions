from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = defaultdict(int)

        for num in nums:
            my_dict[num] += 1

            if my_dict[num] > 1:
                return True
        return False
