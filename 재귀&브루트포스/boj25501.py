def recursion(S, l, r, cnt):
    if l >= r:
        return (1, cnt)
    elif S[l] != S[r]:
        return (0, cnt)
    else:
        return recursion(S, l+1, r-1, cnt + 1)

def isPalindrome(S):
    return recursion(S, 0, len(S) - 1,1)

T = int(input())
cases = []
for t in range(T):
    cases.append(input())
    
for case in cases:
    result = isPalindrome(case)
    print(result[0], result[1])