y,x = map(int,input().split())

a = []
aa = ''
for i in range(y):
    aa = input()
    a.append([])
    for j in range(x):
        a[i].append(aa[j])

sjoi = ['S','J','O','I']
count = 0

#지정된 리스트 양끝을 제외한 한가지 값만 삭제
def ereaserl(l):
    ld = []
    for e in range(1,4):
        ld = ['','','','','']
        for i in range(5):
            ld[i] = l[i]
        del(ld[e])
        
        if ld == sjoi:
            return True
    return False

def fsjoi(f, fx, fy, l):
    global count

    if f < 3:
        if fy != 0:
            fsjoi(f+1, fx, fy-1, l + [a[fy-1][fx]])
                    
        if fx != 0:
            fsjoi(f+1, fx-1, fy, l + [a[fy][fx-1]])
                    
        if fy != y-1:
            fsjoi(f+1, fx, fy+1, l + [a[fy+1][fx]])
                    
        if fx != x-1:
            fsjoi(f+1, fx+1, fy, l + [a[fy][fx+1]])
        
    if f == 3:
        print(l)
    #4칸 이동했고, SJOI 순서로 이동 했다면 count 증가
    if f == 3 and l == sjoi:
        count += 1

    #마지막으로 이동한 곳이 'I'이 아니어도 중간값에 'j','o'가 있다면 한번더 실행
    elif f == 3:
        if fy != 0:
            fsjoi(f+1, fx, fy-1, l + [a[fy-1][fx]])
                
        if fx != 0:
            fsjoi(f+1, fx-1, fy, l + [a[fy][fx-1]])
                
        if fy != y-1:
            fsjoi(f+1, fx, fy+1, l + [a[fy+1][fx]])
                
        if fx != x-1:
            fsjoi(f+1, fx+1, fy, l + [a[fy][fx+1]])

    #마지막으로 이동한 곳이 'I'이고 5칸 이동했으면 실행
    if f == 4:
        print(l)
        #양 끝을 제외한 곳을 단 한번만 지웠을때 SJOI가 된다면 count를 1증가
        if ereaserl(l):
            count += 1

#S 찾기
for fsy in range(y):
    for fsx in range(x):
        if a[fsy][fsx] == sjoi[0]:
            fsjoi(0, fsx, fsy, ['S'])

#SJOI 찾은 횟수      
print(count)
