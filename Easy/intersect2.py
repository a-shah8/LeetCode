# Intersection of 2 arrays

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        counter = None
        result = []
        
        if len(nums1) < len(nums2):
            counter = collections.Counter(nums1)
            
            for n in nums2:
                if n in counter and counter[n] > 0:
                    counter[n] -= 1
                    result.append(n)
        else:
            counter = collections.Counter(nums2)
            
            for n in nums1:
                if n in counter and counter[n] > 0:
                    counter[n] -= 1
                    result.append(n)
        
        return result
