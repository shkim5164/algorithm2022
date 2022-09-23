from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    foward_job = 0
    add_answer = 1
    
    for index in range(0, len(progresses)):
        progress = progresses[index]
        speed = speeds[index]
        remain_day = math.ceil((100 - progress) / speed)
        if foward_job >= remain_day:
            add_answer += 1
        else:
            foward_job = remain_day
            if index != 0 :
                answer.append(add_answer)
            add_answer = 1
            
    answer.append(add_answer)     
    return answer
    
    
    