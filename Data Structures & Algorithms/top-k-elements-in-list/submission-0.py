class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():
            bucket[count].append(num)

        output = []
        for i in range(len(bucket) - 1, -1, -1):
            for b in bucket[i]:
                output.append(b)

                if len(output) == k:
                    return output



        return []


        