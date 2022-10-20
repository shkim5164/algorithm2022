def get_network(index, computers):
    is_network = False
    for i, com in enumerate(computers[index]):
        if index == i or com == 2 or com == 0:
            continue
        if com == 1:
            is_network = True
            computers[index][i] = 2
            computers[i][index] = 2
            get_network(i, computers)
    if is_network :
        return 1 
    return 0
    
def solution(n, computers):
    answer = 0
    for index, computer in enumerate(computers):
        if sum(computer) == 1:
            answer += 1
        else:
            answer += get_network(index, computers)
            
    return answer