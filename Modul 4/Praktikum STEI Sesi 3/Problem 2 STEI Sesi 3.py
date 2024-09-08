#Problem 2 Praktikum STEI Sesi 3
m = int(input('Masukkan nilai m: ')) 
n = int(input('Masukkan nilai n: '))
print('masukkan elemen matriks')
array = [list(map(int,input().split())) for i in range(m)]
array_dummy = [[0 for j in range(n+1)] for i in range(m+1)]
array_new = [[0 for i in range(n)] for i in range(m)]

p = 0
q = 0

#pojok kiri atas (CEK)
array_new[0][0] = array[0][1] + array[1][0]

##pojok kiri bawah (CEK)
array_new[m-1][0] = array[m-2][0]+array[m-1][1]

##pojok kanan atas (CEK)
array_new[0][n-1] = array[0][n-2]+array[1][n-1]

#pojok kanan bawah (CEK)
array_new[m-1][n-1] = array[m-2][n-1]+array[m-1][n-2]

#untuk kolom ujung kiri (CEK)
for i in range(1,m-1) :
    array_new[i][0] = array[i-1][0]+array[i][1]+array[i+1][0]

#untuk kolom ujung kanan (CEK)
for i in range(1,m-1) :
    array_new[i][n-1] = array[i-1][n-1] + array[i][n-2]+array[i+1][n-1]

#baris atas (CEK)
for i in range(1,n-1) :
    array_new[0][i] = array[0][i-1] + array[0][i+1] + array[1][i]

#baris bawah (CEK)
for i in range(1,n-1) :
    array_new[m-1][i] = array[m-1][i-1] + array[m-1][i+1] + array[m-2][i]

#baris sisa (CEK)
for i in range (1,m-1) :
    for j in range(1,n-1) :
        array_new[i][j] = array[i][j-1]+array[i][j+1]+array[i-1][j]+array[i+1][j]

print('--------------')
for i in range(m) :
    for j in range(n) :
        print(array_new[i][j], end=' ')
    print()