stu_list = []
cpr_list = []
bad_list = []
for i in range(28):
    stu_list.append(int(input()))
for i in range(1,31):
    cpr_list.append(i)
bad_list = set(cpr_list) - set(stu_list)
a,b = bad_list

def max_value(a,b):
    return a if a > b else b
def min_value(a,b):
    return a if a < b else b

print(min_value(a,b))
print(max_value(a,b))

    