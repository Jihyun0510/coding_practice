import heapq
import sys

heap = []
n = int(input())
for _ in range(n):
    # x = int(input())
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x),x))

     