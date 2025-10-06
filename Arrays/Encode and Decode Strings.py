from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the delimiter '#' to get the length
            while s[j] != '#':
                j += 1

            # Extract the length and convert to integer
            length = int(s[i:j])

            # Move 'i' past the length and the delimiter
            i = j + 1

            # Extract the string using the calculated length
            j = i + length
            res.append(s[i:j])

            # Move 'i' to the start of the next encoded string
            i = j
        return res
