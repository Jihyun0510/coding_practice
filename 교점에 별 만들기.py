def solution(line):
    # 교점 찾기
    intersections = []

    xs = []
    ys = []
    for a, b, e in line:
        for c, d, f in line:

            # 기울기가 같지 않다면
            if a != c:
                # prevnt division by zero
                if a*d != b*c and a*d != b*c:
                    x = (b*f-e*d)/(a*d-b*c)
                    y = -(e*c-a*f)/(a*d-b*c)
                    # 정수일 때
                    if x%1==0 and y%1==0 and [int(x),int(y)] not in intersections:
                        x = int(x)
                        y = int(y)
                        intersections.append([x, y])
                        # min_x = min(min_x, x)
                        # max_x = max(max_x, x)
                        # min_y = min(min_y, y)
                        # max_y = max(max_y, y)
                        xs.append(x)
                        ys.append(y)

    
    max_y = max(ys)
    min_y = min(ys)
    max_x = max(xs)
    min_x = min(xs)
    
    # status = False

    answer = [['.'] * (max_x-min_x+1) for i in range(max_y-min_y+1)]
    for x, y in intersections:
        answer[y-min_y][x-min_x] = '*'
    for i in range(len(answer)):
        answer[i] = ''.join(answer[i])
    
    
    return answer