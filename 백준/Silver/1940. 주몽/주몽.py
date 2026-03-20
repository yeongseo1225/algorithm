import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int,input().split()))
arr.sort()

start_idx = 0
end_idx = N - 1
count = 0
current_sum = 0

while start_idx < end_idx:
    current_sum = arr[start_idx] + arr[end_idx]
    if M == current_sum:
        start_idx += 1
        end_idx -= 1
        count +=1
    elif M < current_sum:
        end_idx -= 1
    else:
        start_idx += 1
        
print(count)