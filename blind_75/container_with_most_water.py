class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            shorterVert = min(height[left], height[right])
            curArea = shorterVert * (right-left)
            maxArea = max(curArea, maxArea)
            
            #move left by 1 if left is the shorterVert
            if height[left] < height[right]:
                left += 1
            else:
                #move right by 1 if right is the shorterVert
                right -= 1
        return maxArea
