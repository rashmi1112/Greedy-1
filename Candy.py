// TC: O(N) as we will be traversing all the elements in the given array
// SC: O(N) since we store the temporary result in an array of size equal to the input array.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        if not ratings or len(ratings) == 0: 
            return 0
        
        result = [1]*len(ratings)
        
        for i in range(1, len(ratings)): 
            if ratings[i] > ratings[i - 1]: 
                result[i] = result[i - 1] + 1
        
        for i in range(0,len(ratings) - 1)[::-1]: 
            if ratings[i] > ratings[i + 1]:
                result[i] = max(result[i], result[i + 1] + 1)
                
        return sum(result)
