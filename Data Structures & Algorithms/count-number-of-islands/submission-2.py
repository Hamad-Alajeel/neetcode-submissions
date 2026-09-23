class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Tells us if we've visited an island or not
        len_i = len(grid)
        len_j = len(grid[0])
        count = 0
        visited = {}
        # Let's start from top right and go all the way down
        for i in range(len_i):
            for j in range(len_j):
                if grid[i][j] == "1" and not visited.get((i,j),False):
                    # dfs
                    visited[(i,j)] = True
                    heap = deque([(i,j)])
                    # Something here. We can only extend
                    while heap:
                        x,y = heap.popleft()
                        visited[(x,y)] = True
                        grid[x][y] = 0 
                        pos_locs = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
                        for loc in pos_locs:
                            if 0 <= loc[0] < len_i and 0 <= loc[1] < len_j and grid[loc[0]][loc[1]] == "1" and not visited.get((loc[0],loc[1]), False):
                                heap.append(loc)
                                visited[loc] = True
                    count += 1
        return count
                    
                        

                    
                    
