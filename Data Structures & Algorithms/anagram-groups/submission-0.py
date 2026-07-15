class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        d3 = {}

        for word in strs:
            new = "".join(sorted(word))
            result.append(new)
            if new not in d3:
                d3[new] = []
            d3[new].append(word)

        asli = []

        for item in d3:
            asli.append(d3[item])

        return asli 

        






















            