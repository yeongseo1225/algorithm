def solution(num_list, n):
    column = len(num_list)//n
    row = n
    answer = [[0]* n for _ in range(column)]
    a = 0
    for i in range(column):
        for j in range(row):
            answer[i][j] = num_list[a]
            a += 1
            
            
    return answer