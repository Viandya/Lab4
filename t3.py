import random


def q(a, l, r):
    i = l
    j = r
    p = a[(l + r) // 2][0]
    while i <= j:
        while a[i][0] < p:
            i += 1
        while a[j][0] > p:
            j -= 1
        if i <= j:
            a[i][0], a[j][0] = a[j][0], a[i][0]
            i += 1
            j -= 1
    if l < j:
        q(a, l, j)
    if i < r:
        q(a, i, r)


n = int(input())
m = int(input())
a = [[random.randint(5, 61) for j in range(m)] for i in range(n)]
for r in a:
    print(*r)
q(a, 0, n - 1)
print()
for r in a:
    print(*r)
