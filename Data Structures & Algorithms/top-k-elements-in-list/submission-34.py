from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)

        # We iterate through the list to count the frequency of each element
        for num in nums:
            count_dict[num] += 1 
        
        # This line doesn't work here because sorting count_dict.items()
        # returns a list of tuples [(k, v), (k, v))]
        # sorted_list = sorted(count_dict.items(), key=lambda x:x[1], reverse=True)

        # Here, we sort the dictionary keys by their values -> return a list [k, v, x]
        sorted_keys = sorted(count_dict.keys(), key=lambda x:count_dict[x], reverse=True)
        
        # Here, we simply slice the list to retrieve the first two elements
        return sorted_keys[:k]
        
