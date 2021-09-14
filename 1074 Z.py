n, r, c = map(int, input().split())

answer=0
for i in range(n):
    if i == 1:
        if r%2 == 1: answer += 2
        if c%2 == 1: answer += 1
    else:
        if r%(2**(i-1)) == 0:
                answer += ((2**(2*i-1))
        if c%(2**(i-1)) == 0:
                answer += ((2**(2*i-2))
    

print(answer)
