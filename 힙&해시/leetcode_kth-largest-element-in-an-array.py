import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while nums:
            if len(nums) == k:
                return nums[0]
            else:
                heapq.heappop(nums)