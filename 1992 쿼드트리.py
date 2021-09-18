# tree = [['1','1','1','1','0','0','0','0'], ['1','1','1','1','0','0','0','0'], ['0','0','0','1','1','1','0','0'], ['0','0','0','1','1','1','0','0'],
# ['1','1','1','1','0','0','0','0'], ['1','1','1','1','0','0','0','0'], ['1','1','1','1','0','0','1','1'],['1','1','1','1','0','0','1','1']]

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
        
    if length == 2:
        answer.append('('+tree[i][j]+tree[i][j+1]+tree[i+1][j]+tree[i+1][j+1]+')')
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

