
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = list(map(int, input().split()))
    f = [0]
    h = a[0]
    for i in range(1,n):
        if a[i] < h:
            f.append(-1)
        else:     
            f.append(i)
            h = a[i]
    c = 0
    for i in range(n):
        if f[i] != -1 and f[i]<=k[i]:
            c += 1
    print(c)


