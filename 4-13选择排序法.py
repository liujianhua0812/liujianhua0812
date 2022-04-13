a = [3, 8, 17, 6, 9, 22, 5, 35, 99, 1]
l = len(a)
for i in range(l):
    for j in range(i, l):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)

