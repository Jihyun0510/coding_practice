def solution(numbers):
    answer = []
    for num in numbers:
        if not num%2:
            answer.append(num+1)
        else:
            new = bin(num)[2:]
            if len(set(new))==1:
                # print(new)
                x = '10' + bin(num)[3:]
                answer.append(int(x,2))
            else:
                new = list(new)
                for i in range(len(new)-1, -1, -1):
                    if new[i] == '0':
                        new[i] = '1'
                        new[i+1] = '0'                        
                        new = ''.join(new)
                        # print(new)
                        break
                answer.append(int(new,2))                        
    return answer