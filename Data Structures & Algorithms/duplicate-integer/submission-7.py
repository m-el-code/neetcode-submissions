class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                return True
        
        return False