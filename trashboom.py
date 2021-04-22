x, y, n = map(int, input().split())

txy = []
inxy = [0 for i in range(2)]

for xy in range(n):
    inxy = list(map(int, input().split()))
    txy.append([])
    txy[xy] = inxy

a = 0
b = 0

count = 0

def fline(tx, ty):
    global a
    global b
    global count

    if tx == 0 or ty == 0:
        a = 0
        b = 0
        count = n
        
    elif x == 0 and y == 0:
        a = ty / tx
        b = 0
    else:
        a = abs(ty - y) / abs(tx - x)
        b = ty - (tx * a)

def fpoint():
    global count
    c = 0
    
    for f in range(n):
        if txy[f][1] == (txy[f][0] * a) + b:
            c += 1

    if c > count:
        count = c

for b in range(n):
    fline(txy[b][0],txy[b][1])
    fpoint()

print(count)
