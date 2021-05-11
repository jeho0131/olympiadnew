n = int(input())

blockl = []

def block(lb, bn, l):
    global blockl
    
    if bn == 0:
        blockl.append(l)
        
    else:
        if lb <= bn:
            for i in range(1,lb+1):
                block(i, bn - i, l + [i])
                
        elif lb > bn:
            for j in range(1, bn+1):
                block(j, bn - j, l + [j])

for i in range(1,n+1):
    block(i, n-i, [i])

blockl.reverse()

for p in range(len(blockl)):
    for pp in range(len(blockl[p])):
        print(blockl[p][pp], end=' ')
    print()
