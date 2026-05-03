class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            length = str(len(string))
            hashtag = '#'
            encoded_string += length + hashtag + string

        return encoded_string

    def decode(self, encoded_string: str) -> List[str]:
        res = []
        i = 0

        while i < len(encoded_string):
            # Search for '#' starting from our current pointer position 'i'
            j = encoded_string.find("#", i)

            # Extract the number trapped between index i and index j
            length = int(encoded_string[i:j])

            # Extract the word starting after the '#' for 'length' characters
            word = encoded_string[j + 1 : j + 1 + length]
            res.append(word)  # Drop it in our backpack

            # Move the pointer 'i' to the end of the word we just extracted
            i = j + 1 + length
        
        return res

            
