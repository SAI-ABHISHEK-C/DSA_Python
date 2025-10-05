from typing import List

class Search:
    def findIndex (self, nums: List[int], target: int):
        l =[]
        for i , x in enumerate(nums):
            if x == target:
                l.append(i)
        if len(l) > 1:
            return l
        elif len(l) == 1:
            return l[0]
        else:
            return -1
s = Search()
print(s.findIndex([1,2,3], 5))