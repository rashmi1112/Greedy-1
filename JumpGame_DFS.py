class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0: 
            return True
        
        if len(nums) == 1: 
            return True
        
        visited = set()
        
        def dfs(idx): 
#             base 
            if idx == len(nums) - 1: 
                return True
#             logic 
            visited.add(idx)
            for i in range(1, nums[idx] + 1):
                new_idx = idx + i 
                if new_idx not in visited and new_idx < len(nums) and dfs(new_idx): 
                        return True
            return False
            
        return dfs(0)
