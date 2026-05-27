class Solution:
    def rec(self,n,dp):
     
        if n == 1 or  n == 0:
            return 1
        if dp[n]!=-1:
            return  dp[n]
        dp[n-1] = self.rec(n-1,dp)
        dp[n-2] = self.rec(n-2,dp)
        return dp[n-1] + dp[n-2]
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)

        return self.rec(n,dp)
        
