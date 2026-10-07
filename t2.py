import random


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


n = int(input())
a = [random.randint(50, 100) for i in range(n)]
print(*a)
q(a, 0, n - 1)
print(*a)
