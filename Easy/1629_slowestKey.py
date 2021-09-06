class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        
        longest = releaseTimes[0]
        slowestKey = keysPressed[0]
        
        for i in range(1, len(releaseTimes)):
            
            cur = releaseTimes[i] - releaseTimes[i-1]
            if (cur > longest or (cur==longest and keysPressed[i] > slowestKey)):
                longest = cur
                slowestKey = keysPressed[i]
                
        return slowestKey
