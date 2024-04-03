l = ['alice', 'eve', 'charlie', 'gerth', 'ivan', 'C']
n = len(l)

for i in range(n):
    for j in range(0, n - 1):
        if len(l[j]) > len(l[j + 1]):
            t = l[j]
            l[j] = l[j + 1]
            l[j + 1] = t

print(l)
