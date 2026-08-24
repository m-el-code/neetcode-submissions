class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        i = 1
        triangle = []
        for i in range(numRows):
            triangle.append([1]* (i+1))

        for i in range(2, numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle



