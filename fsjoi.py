y, x = map(int, input().split())

a = []
aa = ''
for i in range(y):
    aa = input()
    a.append([])
    for j in range(x):
        a[i].append(aa[j])

SJOI = ['S','J','O','I']
find = ['','','','']
count = 0

def findf(n):
    for i in range(n,4):
        find[i] = ''

def sjoi(f, fx, fy):
    global count
    
    if f < 3:
        if a[fy][fx] == SJOI[f] or f == 0:
            if fy != 0:
                sjoi(f+1, fx, fy-1)
                
            if fx != 0:
                sjoi(f+1, fx-1, fy)
                
            if fy != y-1:
                sjoi(f+1, fx, fy+1)
                
            if fx != x-1:
                sjoi(f+1, fx+1, fy)
   
    if f == 3 and a[fy][fx] == 'I':
        count += 1

for fsy in range(y):
    for fsx in range(x):
        if a[fsy][fsx] == SJOI[0]:
            sjoi(0, fsx, fsy)
            
print(count)
