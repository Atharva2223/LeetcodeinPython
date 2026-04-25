class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def solve(idx, subset):
            if idx == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[idx])
            solve(idx+1, subset)
            subset.pop()
            solve(idx+1, subset)
        solve(0, [])
        return result
