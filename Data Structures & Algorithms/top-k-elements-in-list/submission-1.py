class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = defaultdict(list)
        for t, c in count.items():
            bucket[c].append(t)

        maximum = len(nums)
        output = []
        for i in range(maximum, -1, -1):
            for num in bucket[i]:
                output.append(num)

                if len(output) == k:
                    return output


        



        


        