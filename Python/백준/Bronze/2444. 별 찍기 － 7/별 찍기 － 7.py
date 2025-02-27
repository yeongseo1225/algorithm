N = int(input())
#별
# 1 3 5 7 
# 9 7 5 3 1
# 1 + 2j
#공백
# 4 3 2 1 
# 0 1 2 3 4
for i in range(1,N):
    print(" " * (N-i) + "*" * ((2*i)-1))
for i in range(N,0,-1): 
    print(" " * (N-i) + "*" * ((2*i)-1)) 
    