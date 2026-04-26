class Solution:

    def parentheses_solver(self, index, total,brackets,result):


        if index >= len(brackets):
            if total == 0:
                result.append("".join(brackets))
            return
        if total > len(brackets)//2:
            return
        
        if total < 0:
            return



        brackets[index] = "("
        sum = total+1
        self.parentheses_solver(index+1,sum,brackets,result)

        brackets[index] = ")"
        sum = total-1
        self.parentheses_solver(index+1,sum,brackets,result)
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""] * (n*2)
        result = []
        self.parentheses_solver(0, 0, brackets, result)
        return result

        