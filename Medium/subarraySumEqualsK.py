## Using HashMap - {sum: timesSumOccured}

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count, total = 0, 0
        sum_map = {}
        sum_map[0] = 1
        
        for n in nums:
            total += n
            if total-k in sum_map:
                count += (sum_map[total-k])
            sum_map[total] = sum_map.get(total, 0)+1
            
        return count
