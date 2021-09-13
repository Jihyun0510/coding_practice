n, r, c = map(int, input().split())

answer = 8*(r//2) + 4*(c//2)
if r%2 == 1: answer += 2
if c%2 == 1: answer += 1

print(answer)
