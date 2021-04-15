n = int(input())
s = [[0 for i in range(2)]for j in range(n)]

for k in range(n):
    s[k] = list(map(int, input().split()))

bigc = 0
c = [0 for l in range(2)]

def csf(sn):
    global c
    count = 0
    
    if sn[0] < sn[1]:
        for i in range(1, sn[0]+1):
            if sn[0] % i == 0 and sn[1] % i == 0:
                c[0] = int(sn[0] / i)
                c[1] = int(sn[1] / i)
                count += 1
                
    if sn[0] > sn[1]:
        for j in range(1, sn[1]+1):
            if sn[0] % j == 0 and sn[1] % j == 0:
                c[0] = int(sn[0] / j)
                c[1] = int(sn[1] / j)
                count += 1
                
    if sn[0] == sn[1]:
        c[0] = 1
        c[1] = 1
        count += 1

    if count == 0:
        c[0] = sn[0]
        c[1] = sn[1]

def finds(i, ns):
    global bigc
    count = 0

    if len(ns) > i:
        for f in range(i, n):
            if ns[i][0] == ns[f][0] and ns[i][1] == ns[f][1]:
                count += 1
        finds(i+1, ns)

    if bigc < count:
        bigc = count

ns = []

for cn in range(n):
    csf(s[cn])
    ns.append([])
    ns[cn].append(c[0])
    ns[cn].append(c[1])
print(ns)

finds(0,ns)
print(bigc)
