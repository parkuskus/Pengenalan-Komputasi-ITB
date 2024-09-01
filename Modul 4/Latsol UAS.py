n = int(input('Masukkan nilai n: '))
m = int(input('Masukkan nilai m: '))
array = [list(map(int,input().split())) for i in range(n)]

jumlah_elemen = n*m
elemen_nol = 0
for i in range(n) :
    for j in range(m) :
        if array[i][j] == 0 :
            elemen_nol += 1

sparsity = elemen_nol/jumlah_elemen

if sparsity >= 0.25 :
    print(f'Matriks sparse karena sparsity matrix = {float(sparsity*100)}%')
else :
    print(f'Matriks tidak sparse karena sparsity matriks = {float(sparsity)*100}%')