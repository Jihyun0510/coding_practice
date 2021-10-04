from collections import deque
import sys

t = int(input())

for _ in range(t):
    p = input()
    reverse = False
    n = int(input())
    case = deque(input()[1:-1].split(','))

    for op in p:
        if op == 'R': 
            if reverse:
                reverse = False
            elif not reverse:
                reverse = True
            #     if func == 'R':
            # direction = not direction
        else:
            if not reverse and n:
                case.popleft()
                n -= 1
            elif reverse and n:
                case.pop()
                n -= 1
            else:
                print('error')
                break
    else:
        if not reverse:
            print("["+",".join(case)+"]")
        elif reverse:
            case.reverse()
            print("["+",".join(case)+"]")