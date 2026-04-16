from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        output_dict = defaultdict(list)

        for string in strs:
            # Sort strings
            sorted_string = ''.join(sorted(string))

            # With the usage of defaultdict(list), it 
            # is easier as Python will automatically 
            # match sorted key with the actual value
            # of the original string
            output_dict[sorted_string].append(string)

        # Return the values of the dictionary as a list 
        return list(output_dict.values())
