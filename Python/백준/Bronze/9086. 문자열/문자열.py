T = int(input())#테스트 케이스 개수
for i in range(T):
    s = input()
    s_len = len(s)
    print(f"{s[0]}{s[(s_len-1)]}")