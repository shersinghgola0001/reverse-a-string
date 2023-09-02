def rev(n):
    m = ' '
    index=len(n)
    while index>0:
        m+=n[index-1]
        index=index-1
    return m
print(rev('1234abcd'))
