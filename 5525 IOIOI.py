import sys
n = int(input())
# m = int(sys.stdin.readline().rstrip())
m = int(input())
# s = sys.stdin.readline().rstrip()
s = input()
answer = 0
rep = 0
for i in range(1,m-1):
    if s[i] == 'O' and  s[i-1] == 'I' and s[i+1] == 'I':
        rep += 1
        if rep == n:
            answer += 1
            rep -= 1
    elif s[i] == 'I' and s[i-1] == 'O' and s[i+1] == 'O':
        continue
    else:
        rep = 0

print(answer)