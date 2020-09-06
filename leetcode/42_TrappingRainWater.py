class Solution:
    def trap(self, height) -> int:
        stk = []
        volume = 0
        
        for i in range(len(height)):
            while stk and height[i] > height[stk[-1]]:
                top = stk.pop()
                
                if not len(stk):
                    break
                
                dis = i - stk[-1] - 1
                waters = min(height[i], height[stk[-1]]) - height[top]
                
                volume += dis*waters
            
            stk.append(i)
        
        return volume