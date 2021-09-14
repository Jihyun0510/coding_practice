n, r, c = map(int, input().split())

def cal(n, row, col):
        num = 0
        x=2**i
        if r > x/2-1:
            num += (x*x/2)
        if c > x/2-1:
            num += (x*x/4)
        return num

answer=0

if r%2 == 1: answer += 2
if c%2 == 1: answer += 1   
for i in range(n, 1, -1):
    answer += cal(i, r, c)   
    x = 2**i
    r = r-x/2 if r-x/2>=0 else r
    c = c-x/2 if c-x/2>=0 else c
     
print(int(answer))
