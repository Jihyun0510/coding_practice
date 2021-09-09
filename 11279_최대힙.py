import heapq

heap = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, -x)
    else:
        try: 
            print(-heapq.heappop(heap))
        except:
            print(0)