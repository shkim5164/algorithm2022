from collections import deque

def solution(prices):
    q_prices = deque(prices)
    answer = list()
    
    while q_prices:
        days = 0
        target = q_prices.popleft()
        for price in q_prices:
            days += 1
            if price < target:
                break
                
        answer.append(days)
    return answer

# 40분 남김