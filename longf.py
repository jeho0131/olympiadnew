n = int(input())
s = input()

innum = 0

def zofind(m, x, num):
    global innum

    if s[x] == m:
        if x <= n-2:
            zofind(m, x+1, num+1)
        else:
            if innum < num:
                innum = num+1

    else:
        if innum < num:
            innum = num

for i in range(len(s)):
    if i < len(s)-1:
        if s[i] == '0' and s[i+1] == '0':
            zofind('0', i, 0)
        elif s[i] == '1' and s[i+1] == '1':
            zofind('1', i, 0)

print(innum)
