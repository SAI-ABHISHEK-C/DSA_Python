
from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
c = Solution()
print(c.hasDuplicate([1,2,3,4]))