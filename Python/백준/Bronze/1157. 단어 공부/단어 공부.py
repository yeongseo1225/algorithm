word = input().upper()
char_count = {} #문자 개수를 저장할 딕셔너리

for char in word:
    char_count[char] = char_count.get(char,0)+1
    
max_count = max(char_count.values())

max_chars = [char for char, count in char_count.items() if count == max_count]
    
print(max_chars[0] if len(max_chars) == 1 else "?")