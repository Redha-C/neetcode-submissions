class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for string in strs:
            sorted_string = ''.join(sorted(string))

            my_dict[sorted_string].append(string)

        return list(my_dict.values())



        