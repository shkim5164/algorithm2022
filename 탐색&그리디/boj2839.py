N = int(input())

five = N // 5
while five:
    last_N = N - (five * 5)
    if last_N % 3 == 0:
            break
    five -= 1
    
if five != 0:
    print(five + (last_N // 3))
elif N % 3 == 0:
    print(N // 3)
else:
    print(-1)