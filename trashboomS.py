x, y, n = map(int, input().split())

txy = []

for i in range(n):
    txy.append(list(map(int, input().split())))

a = 0
b = 0

count = 0

def fline(tx, ty):
    global a, b, count
        
    if x == 0 and y == 0:
        a = ty / tx
        b = 0
        
    else:
        a = abs(ty - y) / abs(tx - x)
        b = ty - (tx * a)

# line 구하기

for f in txy:
    fline(f[0],f[1])
    c = 0

    #a,b를 구한 상태에서 쓰레기 갯수구하기
    for g in txy:
        if g[1]==(g[0]*a)+b:
            c += 1

    if count < c:
        count = c


print(count)
