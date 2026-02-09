def solution(s):
    str_list = s.split()
    int_list = [int(x) for x in str_list]
    min_num = min(int_list)
    max_num = max(int_list)
    answer = str(min_num) + " " + str(max_num)
    return answer