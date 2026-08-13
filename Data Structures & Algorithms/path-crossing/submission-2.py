class Solution:
    def isPathCrossing(self, path: str) -> bool:
       
        visited = set()
        x,y = 0,0
        #N, S, E, W
        directions = {'N': [0,1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}

        for d in path:
            visited.add((x, y))
            dx, dy = directions[d]
            x, y = x + dx, y + dy
            if (x,y) in visited:
                return True
        return False

      

            

        
                
