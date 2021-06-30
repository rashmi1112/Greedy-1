# TC: O(N) since we are just iterating over all the elements
# SC: O(1) as we do not need any extra space.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0: 
            return True
        
        if len(nums) == 1: 
            return True
        
        target = len(nums) - 1
        
        for i in range(0, len(nums) - 1)[::-1]: 
            if i + nums[i] >= target: 
                target = i
        
        return target == 0 
