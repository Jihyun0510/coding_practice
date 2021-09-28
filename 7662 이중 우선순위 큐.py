import heapq
import sys
t = int(input())
for _ in range(t):
    q = []
    # inv_q = []

    k = int(input())
    for _ in range(k):
        a,b = input().split()
        if a == 'I':
            heapq.heappush(q, int(b))
            # print(q)
            # heapq.heappush(inv_q, -int(b))
            # print(q)
            # print(inv_q)

        elif a == 'D':
            try:
                if int(b) >= 0:
                    q.pop()
                    # print(q)
                elif int(b) < 0: 
                    heapq.heappop(q)
                    # print(q)
            except:
                continue
    if len(q) > 0:
        print(q[-1], q[0])    
    else:
        print('EMPTY')
