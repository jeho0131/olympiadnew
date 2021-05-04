y, x = map(int, input().split())

a = []
aa = ''
for i in range(y):
    aa = input()
    a.append([])
    for j in range(x):
        a[i].append(aa[j])

SJOI = ['S','J','O','I']
fsjoi = []
count = 0

#리스트 생성
def makel(l):
    global fsjoi
    
    fsjoi.append([])
    fsjoi[len(fsjoi)-1] = l

#지정된 리스트 양끝을 제외한 한가지 값만 삭제
def ereaserl(l):
    ld = []
    for e in range(1,4):
        ld = l
        del(ld[e])
        
        if ld == SJOI:
            return True
    return False

#SJOI값 찾기
def sjoi(f, fx, fy, n):
    global count
    lm = []

    if f == 0:
        if fy != 0:
            lm = ['S',a[fy-1][fx]]
            makel(lm)
            sjoi(f+1, fx, fy-1, len(fsjoi)-1)
                
        if fx != 0:
            lm = ['S',a[fy][fx-1]]
            makel(lm)
            sjoi(f+1, fx-1, fy, len(fsjoi)-1)
                
        if fy != y-1:
            lm = ['S',a[fy+1][fx]]
            makel(lm)
            sjoi(f+1, fx, fy+1, len(fsjoi)-1)
                
        if fx != x-1:
            lm = ['S',a[fy][fx+1]]
            makel(lm)
            sjoi(f+1, fx+1, fy, len(fsjoi)-1)
        
    elif f < 3:
        if fy != 0:
            #현재까지 지나온 값 저장을 하기 위한 리스트 생성
            makel(fsjoi[n])
            #생성한 리스트에 지나갈 값을 저장
            fsjoi[len(fsjoi)-1].append(a[fy-1][fx])
            #다음 값으로 이동
            sjoi(f+1, fx, fy-1, len(fsjoi)-1)
                
        if fx != 0:
            makel(fsjoi[n])
            fsjoi[len(fsjoi)-1].append(a[fy][fx-1])
            sjoi(f+1, fx-1, fy, len(fsjoi)-1)
                
        if fy != y-1:
            makel(fsjoi[n])
            fsjoi[len(fsjoi)-1].append(a[fy+1][fx])
            sjoi(f+1, fx, fy+1, len(fsjoi)-1)
                
        if fx != x-1:
            makel(fsjoi[n])
            fsjoi[len(fsjoi)-1].append(a[fy][fx+1])
            sjoi(f+1, fx+1, fy, len(fsjoi)-1)

    #4칸 이동했고, SJOI 순서로 이동 했다면 count 증가
    if f == 3 and fsjoi[n] == SJOI:
        count += 1

    #마지막으로 이동한 곳이 'I'이 아니어도 중간값에 'j','o'가 있다면 한번더 실행
    elif f == 3 and (fsjoi[n].count('J') > 0 and fsjoi[n].count('O') > 0):
        if fy != 0:
            makel(fsjoi[n])
            fsjoi[len(fsjoi)-1].append(a[fy-1][fx])
            sjoi(f+1, fx, fy-1, len(fsjoi)-1)
                
        if fx != 0:
            makel(fsjoi[n])
            fsjoi[len(fsjoi)-1].append(a[fy][fx-1])
            sjoi(f+1, fx-1, fy, len(fsjoi)-1)
                
        if fy != y-1:
            makel(fsjoi[n])
            fsjoi[len(fsjoi)-1].append(a[fy+1][fx])
            sjoi(f+1, fx, fy+1, len(fsjoi)-1)
                
        if fx != x-1:
            makel(fsjoi[n])
            fsjoi[len(fsjoi)-1].append(a[fy][fx+1])
            sjoi(f+1, fx+1, fy, len(fsjoi)-1)

    #마지막으로 이동한 곳이 'I'이고 5칸 이동했으면 실행
    if f == 4:
        #양 끝을 제외한 곳을 단 한번만 지웠을때 SJOI가 된다면 count를 1증가
        if ereaserl(fsjoi[n]):
            count += 1

#S 찾기
for fsy in range(y):
    for fsx in range(x):
        if a[fsy][fsx] == SJOI[0]:
            sjoi(0, fsx, fsy, 0)

#SJOI 찾은 횟수      
print(count)
