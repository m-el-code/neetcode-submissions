class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        oddMax = 0
        evenMin = len(s)

        for c in count.values():
            if c % 2 != 0 :
                oddMax = max(oddMax, c)
            else:
                evenMin = min(evenMin, c)
        return oddMax - evenMin
