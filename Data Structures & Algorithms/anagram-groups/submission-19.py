class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for s in strs:
            string_sorted_list = sorted(s)
            string_sorted = ''.join(string_sorted_list)

            my_dict[string_sorted].append(s)

        return list(my_dict.values())
