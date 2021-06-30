# TC: O(N^M) where N is the number of elements in the array and M is the maximum depth of options we explore for one element. 
# SC: O(H) where H is the height of the recursive stack

class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: 
            return 0 
        
        self.min_jumps = sys.maxsize
        
        def dfs(idx, jumps): 
#             base
            if idx >= len(nums) - 1: 
                self.min_jumps = min(self.min_jumps, jumps)
                return
            
#             logic
            for i in range(1, nums[idx] + 1): 
                new_idx = idx + i
                dfs(new_idx, jumps + 1)
        
        dfs(0, 0)
        return self.min_jumps
