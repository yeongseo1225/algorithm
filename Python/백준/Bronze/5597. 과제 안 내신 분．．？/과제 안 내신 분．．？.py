all_list = []
suc_list = []
fail_list = []

#모든 학생 리스트
for i in range(1,31):
    all_list.append(i)
#과제를 제출한 학생 리스트
for i in range(28):
    suc_list.append(int(input()))
#과제를 내지 않은 학생 찾기
fail_list = list(set(all_list) - set(suc_list))

#출석 번호 순으로 정렬하기
fail_list.sort()
#출석 번호 순으로 출력하기
print(fail_list[0])
print(fail_list[1])
    
