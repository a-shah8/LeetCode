class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maximum = -1
        
        for i in range(len(arr)-1, -1, -1):
            # tmp = arr[i]
            # arr[i] = maximum
            # maximum = max(maximum, tmp)
            arr[i], maximum = maximum, max(maximum, arr[i])
            
        return arr
