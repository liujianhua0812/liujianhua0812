a = [1, 8, 2, 6, 3, 9, 4]
l = len(a)
for i in range(l):
    for j in range(l - i):
        if a[l - j - 1] < a[l - j - 2]:
            a[l - j - 1], a[l - j - 2] = a[l - j - 2], a[l - j - 1]
print(a)


