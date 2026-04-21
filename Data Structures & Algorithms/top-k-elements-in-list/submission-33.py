from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)

        for num in nums:
            count_dict[num] += 1 
        
        sorted_list = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)
        sorted_keys = sorted(count_dict.keys(), key=lambda x:count_dict[x], reverse=True)
        
        return sorted_keys[:k]
        
