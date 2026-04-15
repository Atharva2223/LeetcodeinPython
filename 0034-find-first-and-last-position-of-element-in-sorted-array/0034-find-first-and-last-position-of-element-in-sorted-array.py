class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        res = []
    
        for i in range(0,len(nums)):
            hmap[i] = nums[i]
        print(hmap)
        for key,value in hmap.items():
            if value == target:
                res.append(key)
        if not res:
            final = [-1,-1]
        else:
            final = [res[0],res[-1]]
        return final
