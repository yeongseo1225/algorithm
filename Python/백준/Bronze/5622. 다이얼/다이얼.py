#숫자 1을 걸려면 2초 필요
#한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸림

S = input()
time = 0

def find_num(S):
    if S in ['A','B','C']:
        return 3
    elif S in ['D','E','F']:
        return 4
    elif S in ['G','H','I']:
        return 5
    elif S in ['J','K','L']:
        return 6
    elif S in ['M','N','O']:
        return 7
    elif S in ['P','Q','R','S']:
        return 8
    elif S in ['T','U','V']:
        return 9
    elif S in ['W','X','Y','Z']:
        return 10
    else:
        return 2
   
for i in range(len(S)):
    time += find_num(S[i])
print(time)  

    
    
    
  
    