class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []
        
        def dfs(elements):

            if len(elements) == 0:
                results.append(prev_elements[:])
            
            for e in elements:
                next_element = elements[:]
                next_element.remove(e)

                prev_elements.append(e)
                dfs(next_element)
                prev_elements.pop()


        dfs(nums)
        return results