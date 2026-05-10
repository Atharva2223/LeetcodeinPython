class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = [-1]*n

        stack = []

        for i in range(2*n-1,-1,-1):

            while len(stack) !=0 and nums[i%n] >= stack[-1]:
                stack.pop()
            
            if i<n:

                if len(stack)!=0:
                    res[i] =stack[-1]
            
            stack.append(nums[i%n])
        return res
        