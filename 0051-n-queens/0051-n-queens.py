class Solution:
    def isSafe(self,chess,row,col):

        for i in range(row -1, -1, -1):
            if chess[i][col] == "Q":
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if chess[i][j] == "Q":
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col +1, len(chess))):
            if chess[i][j] == "Q":
                return False
        return True


    def printNqueens(self,chess,row,ans):
        if row == len(chess):
            board = ["".join(r) for r in chess]
            ans.append(board)
            return

        for col in range(0,len(chess)):
            if self.isSafe(chess,row,col) == True:


                chess[row][col] = "Q"
                self.printNqueens(chess, row+1,ans)
                chess[row][col] = "."

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        chess = [["." for _ in range(n)] for _ in range(n)]
        self.printNqueens(chess, 0, ans)
        return ans
