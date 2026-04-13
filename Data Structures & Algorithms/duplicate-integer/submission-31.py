from typing import List 

class Solution():
    def hasDuplicate(self, nums: List[int]) -> bool: 
        seen = ()

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True

