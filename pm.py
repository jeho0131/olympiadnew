num = []
l = int(input())
num = list(map(int, input().split()))
s=0
count=0

def A(i,s):
    global count
    if i < len(num) - 1:
        if s + num[i] < 21:
            A(i+1,s + num[i])
        if s - num[i] > -1:
            A(i+1,s-num[i])

    else:
        if s == num[i]:
            count += 1
            
    
  
    

s = num[0]
A(1,s)
print(count)
