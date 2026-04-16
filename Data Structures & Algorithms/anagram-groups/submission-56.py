from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_list = []
        output_dict = defaultdict(list)

        for string in strs:
            # Sort strings
            sorted_string = ''.join(sorted(string))

            # Append sorted string to a list
            sorted_list.append(sorted_string)

            # If a sorted string is present in sorted_list,
            # we append the original string to the list in 
            # the dictionary 
            if sorted_string in sorted_list:
                output_dict[sorted_string].append(string)

        # Return the values of the dictionary as a list 
        return list(output_dict.values())
