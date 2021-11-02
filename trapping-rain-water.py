class Solution:
    def trap(self, height: List[int]) -> int:
        currentheights = []
        left = 0
        for i in range(len(height)):
            left = max(left, height[i])
            currentheights.append(left)
            
        right = 0
        
        for i in range(len(height) - 1,-1, -1):
            right = max(right, height[i])
            currentheights[i] = min(currentheights[i], right) - height[i]
        
        sum = 0
        for height in currentheights:
            sum += height
        return sum