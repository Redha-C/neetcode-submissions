from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        sorted_list = []
        output_dict = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))
            sorted_list.append(sorted_string)

            if sorted_string in sorted_list:
                output_dict[sorted_string].append(string)

        return list(output_dict.values())
