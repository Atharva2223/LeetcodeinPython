class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)

        cols = len(matrix[0])

        r = [0]*rows
        col =[0]*cols

        for i in range(0,rows):
            for j in range(0,cols):
                if matrix[i][j] == 0:
                    r[i] = -1
                    col[j] = -1
        for i in range(0,rows):
            for j in range(0,cols):
                if r[i] or col[j] == -1:
                    matrix[i][j] = 0


        
        