class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ## Brute-force approach
#         answer = []
#         for q in queries:
#             count = 0
#             for p in points:
#                 count += ((q[0]-p[0])**2 + (q[1]-p[1])**2 <= q[2]**2)
#             answer.append(count)
        
#         return answer

        ## Sorting
        answer = []
        points_xsorted = sorted(points)
        
        for q in queries:
            count = 0
            for p in points_xsorted:
                if q[0]+q[2] < p[0]:
                    break
                count += ((q[0]-p[0])**2 + (q[1]-p[1])**2 <= q[2]**2)
            answer.append(count)
            
        return answer
