## Using 2 heaps
## 'small' heap contains all elements in inverted order (elements are negated before pushed)
## 'large' heap contains all elements larger than 'small' heap

## Time complexity - O(NlogN)
## Space complexity - O(N)

from heapq import heappush, heappushpop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # invert of minheap (maxheap) - contains smaller inverted ordered elements
        self.small = []
        # minheap - contains larger ordered elements
        self.large = []
        

    def addNum(self, num: int) -> None:
        
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        
        return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
