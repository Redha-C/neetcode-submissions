from collections import defaultdict

class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        count_str1 = defaultdict(int)
        count_str2 = defaultdict(int)

        # If length of strings are different -> no anagrams
        if len(str1) != len(str2):
            return False
        
        # Counting the number of characters in string 1
        for char1 in str1:
            count_str1[char1] += 1

        # Counting the number of characters in string 2 
        for char2 in str2:
            count_str2[char2] += 1 

        # Sorting dictionaries by keys
        count_str1_sorted = sorted(count_str1.items())
        count_str2_sorted = sorted(count_str2.items())

        return count_str1_sorted == count_str2_sorted

