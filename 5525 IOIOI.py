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
        answer += 1
print(answer)