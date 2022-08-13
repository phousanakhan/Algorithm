class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l_idx = 0
        r_idx = len(height) - 1
        while l_idx < r_idx:
            #A = L* W
            cur_water = (r_idx - l_idx) * min(height[r_idx],height[l_idx])
            max_water = max(max_water, cur_water)
            if height[r_idx] < height[l_idx]:
                r_idx -= 1
            else:
                l_idx += 1
        return max_water
