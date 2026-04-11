class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []

        result = []

        top,left = 0, 0
        bottom, right = len(matrix)-1,len(matrix[0]) -1

        while top <= bottom and left <= right:

            #move left to right

            for i in range(left,right+1):
                result.append(matrix[top][i])

            top+=1

            # move top to bottom

            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1

            if top <= bottom:
                # right to left
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])

                bottom-=1

            if left <= right:
                # bottom to top
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1

        return result   

            




        