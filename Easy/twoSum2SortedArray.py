## Approach 1 - Using dictionary (Time efficient)
## Approach 2 - Using Binary Search (Space efficient)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ## More space complexity
        
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i


        ## More time complexity
        
#         for i in range(len(numbers)):
#             l, r = i+1, len(numbers)-1
#             second = target - numbers[i]
            
#             while l<=r:
#                 mid = l + (r-l)//2
#                 if numbers[mid] == second:
#                     return [i+1, mid+1]
#                 elif numbers[mid] < second:
#                     l = mid+1
#                 else:
#                     r = mid-1
