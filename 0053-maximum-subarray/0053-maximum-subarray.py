class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       csum = nums[0]
       osum = nums[0]

       n = len(nums)

       for i in range(1,n):
      
        if csum >=0:
            csum+=nums[i]
            
        else:
            csum = nums[i]
        osum=max(osum,csum)
       
       return osum
    