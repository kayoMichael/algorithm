class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maximum = 0
        for i in range(len(heights)):
            start = 0
            while stack and heights[stack[-1][0]] > heights[i]:
                index, width = stack.pop()
                maximum = max(maximum, heights[index] * (i - index + width))
                start += width + 1
            stack.append((i, start))

        start = 0
        while stack:
            index, width = stack.pop()
            start += width + 1
            maximum = max(maximum, heights[index] * start)

        return maximum
