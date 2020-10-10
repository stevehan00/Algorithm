class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort()
        
        for n in nums1:
            i2 = bisect.bisect_left(nums2, n)
            if len(nums2) > 0 and len(nums2) > i2 and n == nums2[i2]:
                result.add(n)
        
        return result