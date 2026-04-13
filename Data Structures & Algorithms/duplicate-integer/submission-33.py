from typing import List 

class Solution():
    def hasDuplicate(self, nums: List[int]) -> bool: 
        seen = set()

        for num in nums:
            # num not in set -> add to set
            if num not in seen:
                seen.add(num)
            # num already in set -> return True
            else:
                return True

        # if no duplicates -> return False
        return False
