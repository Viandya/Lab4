def q(a, l, r):
    i = l
    j = r
    p = a[(l + r) // 2]
    while i <= j:
        while a[i] < p:
            i += 1
        while a[j] > p:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if l < j:
        q(a, l, j)
    if i < r:
        q(a, i, r)


a = list(map(int, input().split()))
q(a, 0, len(a) - 1)
print(*a)
