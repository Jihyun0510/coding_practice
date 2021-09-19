n = int(input())
tree = []
for _  in range(n):
    tree.append(list(input()))

answer = []
def cut(i, j, length):
    
    sol = tree[i][j]
    status = False
    for x in range(i, i+length):
        if set(tree[x][j:j+length]) != set(sol):
            status=True
    if not status:
        answer.append(sol)
        return        

    answer.append('(')
    length = length//2
    cut(i, j, length)
    cut(i, j+length, length)
    cut(i+length, j, length)
    cut(i+length, j+length, length)
    answer.append(')')
    
cut(0, 0, n)
print(''.join(answer))

    # if case ==2:
    #     #print(xs, ys,(xs+xe)//2,(ys+ye)//2 )
    #     elem1= divide_conquer(xs,ys,(xs+xe)//2,(ys+ye)//2) 
    #     elem2= divide_conquer(xs,(ys+ye)//2,(xs+xe)//2,ye) 
    #     elem3= divide_conquer((xs+xe)//2,ys,xe,(ys+ye)//2) 
    #     elem4= divide_conquer((xs+xe)//2,(ys+ye)//2,xe,ye) 
    #     return "("+elem1+elem2+elem3+elem4+")"
    # else:
    #     return str(control)
