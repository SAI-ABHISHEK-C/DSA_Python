# Two Sum Problem

# Tags: Array, Hash Map, Two Pointers (sorted version)
# Difficulty: Easy


from collections import defaultdict
from typing import List, Tuple

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # MY FIRST APPROACH

        # TC ==> O(N²): Big O Notation (Brute-force/worst case)
        # SC ==> O(1)

        '''
        n_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    n_list.append(i)
                    n_list.append(j)
                    return n_list
        '''

        # MY SECOND APPROACH (BEST - for single instances of 2 numbers in the given list)

        """
            Intuition
            ---------
            Store previously seen numbers in a dictionary so each lookup is O(1).
    
            Approach
            --------
            - For each x (number in the original list) and it's index i, 
              compute diff = target - x
            - If need is in the dictionary, return [map[need], i]; else map[x] = i
    
            Complexity
            ----------
            Time: O(n), Space: O(n)
            
            Constraints:
            ----------
            2 <= nums.length <= 10⁴
            -10⁹ <= nums[i] <= 10⁹
            -10⁹ <= target <= 10⁹
    
            Examples
            --------
            >>> two_sum([2,7,11,15], 9) 
            Inputs : [List of numbers], target (int) 
            Output : [0, 1] ==> list of indexes of those 2 numbers in the original list
        """

        # TC ==> O(N) Big-O Notation (Brute-force/worst case)
        # SC ==> O(N)

        seen_nums ={}
        # print("Original List: ",nums)
        # print("Target: ",target)
        # print("Created an empty Dictionary",seen_nums)

        for i , x in enumerate(nums):
            # print("Iteration Number: ",i+1)
            # print("index:",i, "value:",x)
            diff = target - x
            #print(f"difference between target ({target}) and existing number ({x}):",diff)
            if diff in seen_nums:
                # print(f"Yes Difference: ({diff}) is there as a KEY in the dictionary")
                # print(f"Hence returning the VALUE: ({seen_nums[diff]}) of the KEY: ({diff}) and the existing index ({i})")
                return [seen_nums[diff], i]
            # print(f"Not found! ({diff}) as a KEY in the dictionary ({seen_nums}) ")
            # print(f"Hence Storing the number as KEY:({x}) and index as VALUE:({i}) in the created dictionary")
            seen_nums[x] = i
            #print(seen_nums)
        return []

    # Code for finding Two sums if there are multiple instances of 2 numbers which add-on to target number
    # TC ==> O(N²): Big O Notation (Brute-force/worst case)
    # SC ==> O(1)

    '''
        seen_nums = defaultdict(list)  # value will be in list format --> Which would hold the occurances of the number in the original list
        pairs : List[Tuple[int, int]] = []  # Origianl list containing pairs of indexs of numbers (which add-on to get target number) as a tuple
        print("Original List: ",nums)
        print("Target: ",target)
        print("Created an empty Dictionary",seen_nums)
        for j , x in enumerate(nums):
            print("Iteration Number: ",j+1)
            diff = target - x
            print(f"difference between target ({target}) and existing number ({x})",diff)
            if diff in seen_nums:
                print(f"Yes Difference: ({diff}) is there as a KEY in the dictionary")
                print("Hence making a tuple of every value of the list in front of key with the existing index and appending it to the result list")
                for i in seen_nums[diff]:
                    # extracting every value from the list and making it a tuple with existing index and appending it into a list
                    pairs.append((i,j))
                    print("Result list: ",pairs)
            print("Not Found! Hence appending existing index to the numbers list")
            seen_nums[x].append(j)
            print(seen_nums)
        return pairs
    '''

s = Solution()
v = s.twoSum([2,7,15,11],9)
print(v)