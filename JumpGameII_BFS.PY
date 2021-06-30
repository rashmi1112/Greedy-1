# TC: O(N^M) where N is the input array size and M is the maximum ways we are exploring at an index to reach the last index.
# SC: O(N) where N is the size of the queue.

class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: 
            return 0 
        
        queue = collections.deque()
        visited = set()
        queue.append(0)
        visited.add(0)
        jumps = 0
        target = len(nums) - 1
        while queue: 
            # print(jumps)
            size = len(queue)
            for j in range(size): 
                curr = queue.popleft()
                if curr >= target: 
                    return jumps
                for i in range(1, nums[curr] + 1): 
                    new_idx = curr + i
                    if new_idx >= target: 
                        return jumps + 1
                    if not new_idx in visited and new_idx < len(nums): 
                        queue.append(new_idx)
                        visited.add(new_idx)
            jumps += 1
        
        return jumps 
