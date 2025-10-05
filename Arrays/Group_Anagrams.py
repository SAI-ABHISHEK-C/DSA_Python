from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for w in strs:
            key = ''.join(sorted(w))  # or: tuple(sorted(w))
            groups[key].append(w)
        return list(groups.values())


s = Solution()
print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))