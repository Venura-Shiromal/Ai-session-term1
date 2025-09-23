def christmas_tree(h):
    for i in range(h):
        print(('*' * (2*i+1)).center(2*h))

def subs_check(sub, string):
    i = 0
    for char in string:
        if i < len(sub) and char == sub[i]:
            i += 1
    if i == len(sub):
        print("Yes")
    else:
        print("No")