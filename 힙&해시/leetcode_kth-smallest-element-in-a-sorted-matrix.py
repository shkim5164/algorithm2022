import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        all_list = []
        for i in matrix:
            all_list.extend(i)
        
        heapq.heapify(all_list)
        while all_list:
            if k == 1:
                return all_list[0]
            else:
                k -= 1
                heapq.heappop(all_list)