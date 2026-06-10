class Solution:
    def bfs(self,grid,visited,i,j):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        queue.append((i,j))

        while len(queue) !=0:
            x,y = queue.popleft()
            for xx, yy in ([0,-1],[0,1],[-1,0],[1,0]):
                new_x, new_y = x+xx, y+yy

                if new_x < 0 or new_x >= rows or new_y < 0 or new_y >=cols:
                    continue
                if grid[new_x][new_y] == "0":
                    continue
                if visited[new_x][new_y] == 1:
                    continue
                visited[new_x][new_y] = 1
                queue.append((new_x,new_y))

    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c] == 0:
                    count+=1
                    self.bfs(grid,visited,r,c)
        return count