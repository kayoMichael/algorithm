class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)

        for st in strs:
            signature = [0] * 26

            for t in st:
                signature[ord(t) - ord('a')] += 1

            dictionary[tuple(signature)].append(st)

        output = []

        for t, lst in dictionary.items(): 
            output.append(lst)

        return output