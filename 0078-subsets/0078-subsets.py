class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def rec(idx, curr):
            if idx == len(nums):
                ans.append(curr.copy())
                return
            
            # include current element
            curr.append(nums[idx])
            rec(idx + 1, curr)
            
            # exclude current element (backtrack)
            curr.pop()
            rec(idx + 1, curr)
        
        rec(0, [])
        return ans
        