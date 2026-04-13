class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = defaultdict(int)

        for num in nums:
            output[num] += 1
        
        sorted_keys = sorted(output, key=lambda x: output[x], reverse=True)

        return sorted_keys[:k]