n = 8

tree = [['1','1','1','1','0','0','0','0'], ['1','1','1','1','0','0','0','0'], ['0','0','0','1','1','1','0','0'], ['0','0','0','1','1','1','0','0'],
['1','1','1','1','0','0','0','0'], ['1','1','1','1','0','0','0','0'], ['1','1','1','1','0','0','1','1'],['1','1','1','1','0','0','1','1']]

answer = []
def cut(i, j, length):
    answer.append('(')
    if length == 1:
        answer.append(tree[i][j]+tree[i][j+1]+tree[i+1][j]+tree[i+1][j+1])

    else:
        sol = tree[i][j]
        for x in range(length):
            if set(tree[x][j:j+length]) != sol or len(set(tree[x][j:j+length])) != 1:
                cut(i, j, length//2)
                cut(i+length//2, j, length//2)
                cut(i, j+length//2, length//2)
                cut(i+length//2, j+length//2, length//2)
                answer.append(')')
                break
            else:
                answer.append(sol)
    answer.append(')')
    return

cut(0, 0, n)
print(answer)


