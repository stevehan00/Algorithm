class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        results = []
        for i in nums:
            if i not in results:
                results.append(i)
            else:
                results.remove(i)
        return results[0]