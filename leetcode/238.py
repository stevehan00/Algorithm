class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]
        q = [1]
        re = 1
        req = 1

        sol = []
        for i in range(len(nums)-1):
            re *= nums[i]
            req *= nums[len(nums)-i-1]
            p.append(re)
            q.append(req)
        
        for i in range(len(p)):
            sol.append(re[i]*req[len(p)-i-1])
            
        return sol