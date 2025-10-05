from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        strs.sort()
        print(strs)
        first = strs[0]
        last = strs[-1]
        l = []

        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                l.append(first[i])
            else:
                break
        return ''.join(l)

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight","float"]))