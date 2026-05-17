class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    
        
        # monotonic queue!

        queue = deque()
        output = []
        for right in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()

            queue.append(right)

            while queue and queue[0] < right - k + 1:
                queue.popleft()


            if right + 1 >= k:
                output.append(nums[queue[0]])

        return output





            