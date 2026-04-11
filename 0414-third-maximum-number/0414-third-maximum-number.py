class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        prev_element = nums[0]
        ct_element = 1
        for index in range(len(nums)):
            if prev_element != nums[index]:
                ct_element+=1
                prev_element = nums[index]
            
            if ct_element == 3:
                return nums[index]

        return nums[0]
            
        
       