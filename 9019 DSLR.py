from collections import deque
# import sys
# input = sys.stdin.readline

t = int(input())

def bfs():
    q = deque()
    q.append((a, ""))
    visited = set()
    visited.add(a)
    while q:
        now, oper = q.popleft()
        # 정답과 동일할 시 return
        if now == b:
            return oper
        
        # oper = 'D'
        dd = now*2 % 10000
        if dd not in visited:
            visited.add(dd)
            q.append((dd, oper+'D'))
        # oper = 'S'
        sd = now-1 if now!=0 else 9999
        if sd not in visited:
            visited.add(sd)
            q.append((sd, oper+'S'))
        # oper = 'L'
        ld = (now % 1000)*10 + now//1000
        if ld not in visited:
            visited.add(ld)
            q.append((ld, oper+'L'))
        # oper = 'R'
        rd = (now % 10)*1000 + now//10
        if rd not in visited:
            visited.add(rd)
            q.append((rd, oper+'R'))      
        
for _ in range(t):
    a,b=map(int, input().split())
    print(bfs())
