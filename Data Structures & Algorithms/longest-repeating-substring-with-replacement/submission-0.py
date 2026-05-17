class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = total = maximum = 0
        dictionary = defaultdict(int)
        for right in range(len(s)):
            dictionary[s[right]] += 1
            maximum = max(maximum, dictionary[s[right]])
            if right - left + 1 - maximum > k:
                dictionary[s[left]] -= 1
                left += 1

            total = max(total, right - left + 1)

        return total

                