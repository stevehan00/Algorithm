import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Cntr = collections.Counter(nums)
        lst = []
        for c in Cntr.most_common(k):
            lst.append(c[0])
        return lst