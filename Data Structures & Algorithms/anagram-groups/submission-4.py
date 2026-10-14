class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []

        temp_freq = {}

        # loop through the strings
        # create a dict of their letter:freq and then another word:dict
        # if freq is in the freq dict, add strings in temp, and push into final
        for x in strs:
            key = "".join(sorted(x))
            if key in temp_freq:
                temp_freq[key].append(x)
            else:
                temp_freq[key] = [x]
        
        return list(temp_freq.values())