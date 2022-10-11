import itertools

def solution(numbers, target):
    answer = 0
    operators = ['+', '-']
    permutations_with_repeat = list(itertools.product(operators, repeat = len(numbers)))
    for repeat in permutations_with_repeat:
        result = 0
        for index, operator in enumerate(repeat):
            if operator == "+":
                result += numbers[index]
            else:
                result -= numbers[index]
        if result == target:
            answer += 1
    return answer