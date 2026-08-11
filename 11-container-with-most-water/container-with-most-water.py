class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l,r = 0, len(height) - 1

        while l<r:
            subarea = min(height[l], height[r])* (r - l)
            area = max(area, subarea)
            if height[l]< height[r]:
                l+=1
            else:
                r-=1

        return area