m = int(input('Masukkan nilai m: '))
print('Masukkan kondisi papan catur')
print('Hasil papan catur')
array = [list(map(str,input().split())) for i in range(m)]
array_cek = [[0 for j in range(m) for i in range(m)]]
 

status_raja = False

for i in range(m) :
    for j in range(m) :
        #Kebawah
        if (array[i][j] == 'K') and (0 <= i+2 <= m-1) and (0<=j+1<=m-1) : 
            if array[i+2][j+1] == 'R' :
                status_raja = True
        if (array[i][j] == 'K') and (0<=i+2 <= m-1) and (0<=j-1<=m-1) :
            if array[i+2][j-1] == 'R' :
                status_raja = True
        #Keatas
        if (array[i][j] == 'K') and (0<=i-2 <= m-1) and (0<=j+1<=m-1) :
            if array[i-2][j+1] == 'R' :
                status_raja = True
        if (array[i][j] == 'K') and (0<=i-2 <= m-1) and (0<=j-1<=m-1) :
            if array[i-2][j-1] == 'R' :
                status_raja = True
        #Kekanan
        if (array[i][j] == 'K') and (0<= i-1 <= m-1) and (0<=j+2<=m-1) :
            if array[i-1][j+2] == 'R' :
                status_raja = True
        if (array[i][j] == 'K') and (0<= i+1 <= m-1) and (0<= j+2<=m-1) :
            if array[i+1][j+2] == 'R' :
                status_raja = True
        #Kekiri
        if (array[i][j] == 'K') and (0<= i-1 <= m-1) and (0<=j-2<=m-1) :
            if array[i-1][j-2] == 'R' :
                status_raja = True
        if (array[i][j] == 'K') and (0<= i-1 <= m-1) and (0<=j-2<=m-1) :
            if array[i-1][j-2] == 'R' :
                status_raja = True

if status_raja == True :
    print('Raja tidak aman dari serangan kuda')
else :
    print('Raja aman dari serangan kuda')