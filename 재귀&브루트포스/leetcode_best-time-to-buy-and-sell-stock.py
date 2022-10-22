from collections import deque

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        prices = deque(prices)
        start = 100000
        while prices:
            standard = prices.popleft()
            if start >= standard:
                start = standard
                continue
            answer = max(answer, standard - start)
        if answer <= 0:
            return 0
        return answer