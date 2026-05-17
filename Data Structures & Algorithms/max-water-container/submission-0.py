class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = total = 0
        right = len(heights) - 1


        while left < right:
            total = max(total, min(heights[left], heights[right]) * (right - left))

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1


        return total