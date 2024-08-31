t = int(input())
array = [list(map(int, input().split())) for i in range(t)]

y = 0

for i in range(t) :
    for j in range(3) :
        y = array[i][1]-array[i][2]
    if array[i][0] == 0 :
        print('SUMBU')
    elif y>0 :
        print('SATU')
    elif y<0 :
        print('EMPAT')
