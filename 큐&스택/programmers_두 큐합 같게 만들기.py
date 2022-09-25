from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    
    if (sum_q1 + sum_q2) % 2:
        return -1
    else:
        answer = 0
        target = (sum_q1 + sum_q2) // 2
        while answer <= 600000:
            
            if sum_q1 == sum_q2:
                return answer

            if sum_q1 < sum_q2:
                pop_one = queue2.popleft()
                queue1.append(pop_one)
                sum_q2 -= pop_one
                sum_q1 += pop_one
            else:
                pop_one = queue1.popleft()
                queue2.append(pop_one)
                sum_q1 -= pop_one
                sum_q2 += pop_one
                
            answer += 1
        
    return -1