N = int(input())
n_list = list(map(int,input().split()))
min = n_list[0]
max = n_list[0]
for i in n_list:
    if i > max:
        max = i      
    elif i < min:
        min = i
print(min,max) 
        
        
       
        
    