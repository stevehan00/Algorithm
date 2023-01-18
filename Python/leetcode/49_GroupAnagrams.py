import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dt = collections.defaultdict()
        for i in strs:
            dt["".join(sorted(i))].append(i)

        return dt.values()