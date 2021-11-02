class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}
        
        for i in range(len(strs)):
            string = "".join(sorted(strs[i]))
            if (string in dict):
                dict[string].append("".join(strs[i]))
            else:
                dict[string] = ["".join(strs[i])]

        return dict.values()