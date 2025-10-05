from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[n] = nums[i]
                n += 1
        return n


s = Solution()
print(s.removeDuplicates([1,1,2]))