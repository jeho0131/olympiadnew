d = int(input())
A = ["" for i in range(d)]

def rp(i):
    if i < d:
        A[i] = '+'
        rp(i+1)

        A[i] = '-'
        rp(i+1)

        '''A[i] = '*'
        rp(i+1)

        A[i] = '/'
        rp(i+1)'''

    else:
        print("")
        for i in range(d):
            print(A[i], end=" ")

rp(0)
