def solution(num):
    num = list(map(lambda x : str(x), num))
    num.sort(key=lambda x : x*3, reverse=True)
    return str(int("".join(num)))
    