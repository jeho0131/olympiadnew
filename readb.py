r, fb, sb = map(int, input().split())
fp = list(map(int, input().split()))
sp = list(map(int, input().split()))


bigp = 0
def readb(i, p, f, s):
    global bigp
    if i < r:
        if f < len(fp):
            readb(i+1, p+fp[f], f+1, s)
        if s < len(sp):
            readb(i+1, p+sp[s], f, s+1)

    else:
        if bigp < p:
            bigp = p

readb(0, 0, 0, 0)
print(bigp)
