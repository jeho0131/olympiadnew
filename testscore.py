n = int(input())
ns = list(map(int, input().split()))
nb = list(map(int, input().split()))

s = 0
for i in range(n):
    if ns[i] < 30 and nb[i] == 1:
        s += 30

    else:
        s += ns[i]

print(s)
