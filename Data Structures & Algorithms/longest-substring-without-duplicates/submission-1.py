class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = total = 0
        dictionary = defaultdict(int)
        for right in range(len(s)):
            dictionary[s[right]] += 1

            while dictionary[s[right]] >= 2:
                dictionary[s[left]] -= 1
                left += 1

            total = max(total, right - left + 1)


        return total
            
