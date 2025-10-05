from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged_list = nums1 + nums2
    merged_list.sort()
    print(merged_list)

    if len(merged_list) % 2 != 0:
        i = int(len(merged_list) / 2)
        return int(merged_list[i])
    else:
        i = int(len(merged_list) / 2)
        j = i - 1
        k = (merged_list[i] + merged_list[j])/2
        return k

print(findMedianSortedArrays([1,2], [3,4]))