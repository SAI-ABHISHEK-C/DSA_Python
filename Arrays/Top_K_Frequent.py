class Solution:

    def get_key_from_value(self, dictionary, target_value):
        for key, value in dictionary.items():
            if value == target_value:
                return key

    def topKFrequent(self, nums, k):
        d = {}
        l = []
        count = 1
        if len(nums) == k:
            return nums
        for x in nums:
            if x in d.keys():
                d[x] = d[x] + 1
            else:
                d[x] = count

        print(d)
        t = max(d.values())
        v = self.get_key_from_value(d, t)
        for x ,y in d.items():
            if k > 1 and y > k :
                l.append(y)
            elif len(l) == k:
                l.append(v)
        return l




s = Solution()
print(s.topKFrequent([3,0,1,0], 1))