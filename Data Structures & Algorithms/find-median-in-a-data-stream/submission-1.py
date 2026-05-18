class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.running_sum = 0

    def addNum(self, num: int) -> None:
        self.running_sum += num
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.max_heap, -num)

        else:
            heapq.heappush(self.min_heap, num)

        if self.min_heap and self.max_heap and self.min_heap[0] < -self.max_heap[0]:
            val1 = -heapq.heappop(self.max_heap)
            val2 = -heapq.heappop(self.min_heap)

            heapq.heappush(self.min_heap, val1)
            heapq.heappush(self.max_heap, val2)
    def findMedian(self) -> float:
        length = len(self.min_heap) + len(self.max_heap)
        if length % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2

        return -self.max_heap[0]

        