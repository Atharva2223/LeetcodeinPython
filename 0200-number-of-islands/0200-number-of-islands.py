class Solution:

    def dfs(self,visited,grid,r,c):

        rows = len(grid)
        cols = len(grid[0])


        queue = deque()
        queue.append((r,c))
        visited[r][c] = 1

        while len(queue)!=0:
            i,j = queue.popleft()

            for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_x,new_y = x+i,y+j

                if new_x <0 or new_y <0 or new_x >= rows or new_y >= cols:
                    continue
                if grid[new_x][new_y]  == '0':
                    continue
                if visited[new_x][new_y] == 1:
                    continue
                queue.append((new_x,new_y))
                visited[new_x][new_y] =1


    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and visited[r][c] == 0:
                    count+=1
                    self.dfs(visited,grid,r,c)
        return count




        