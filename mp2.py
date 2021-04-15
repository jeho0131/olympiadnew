num = []
l = int(input())
f = int(input())
num = list(map(int, input().split()))
s=0
count=0

def A(i,s):
    global count
    if i < len(num):
        if s + num[i] <= 700:
            A(i+1,s + num[i])
        if s - num[i] > -1:
            A(i+1,s-num[i])
        if s * 10 + num[i] <= 700:
            A(i+1,s * 10 + num[i])

    else:
        if s == f:
            count += 1
        print(s)
            
    
  
    

s = num[0]
A(1,s)
print(count)
