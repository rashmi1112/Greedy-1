# TC: O(N^M) where N is the length of the array and M is the maximum number in the input array, as in worst case, we will be exploring M options for every input element. 
# SC: O(N) where N is the length of length of queue.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0: 
            return True
        
        if len(nums) == 1: 
            return True
        
        visited = set()
        queue = collections.deque()
        queue.append(0)
        visited.add(0)
        
        while queue:
            curr = queue.popleft()
            if curr == len(nums) - 1:
                    return True
            for i in range(1, nums[curr] + 1): 
                new_idx = curr + i
                if new_idx == len(nums) - 1:
                    return True
                if new_idx not in visited and new_idx < len(nums):
                    queue.append(new_idx)
                    visited.add(new_idx)
        
        return False
                    
