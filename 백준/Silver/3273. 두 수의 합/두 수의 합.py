import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

count = 0
current_sum = 0
start_idx = 0
end_idx = n - 1

while start_idx < end_idx:
    current_sum = arr[start_idx] + arr[end_idx]
    if current_sum == x:
        count += 1
        start_idx += 1
        end_idx -= 1
    elif current_sum < x:
        start_idx += 1
    else:
        end_idx -= 1
        
print(count)