from typing import List

class Solution:
    def containsWater(self, nums: List[int]) -> bool:

        # Two Pointer Method

        left = 0
        right = len(nums) - 1
        res = 0
        while left < right:
            amount = min(nums[left], nums[right]) * (right - left)
            res = max(amount, res)
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return res

        # Brute Force Method

        # res = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         amount = min(nums[i], nums[j]) * (j-i)
        #         res = max(amount,res)
        # return res




s = Solution()
print(s.containsWater([1,8,6,2,5,4,8,3,7]))

