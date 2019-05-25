def int2list(n):
    li = []
    while n>0:
        li.append(n%10)
        n /= 10
    return li

