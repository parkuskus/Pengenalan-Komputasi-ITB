#Problem 3 Tugas Pendahuluan Praktikum STEI 2023 
#Input
n = int(input("Masukkan N: "))
m = int(input("Masukkan M: "))
print("Masukkan peta: ")
A = [list(map(int,input().split())) for i in range(n)]

#inisialisasi awal
kapal_array = 0
kapal_total = 0

#pemrosesan data 
for i in range(n) :
    for j in range(m) :
        if A[i][j] == 1 :
            kapal_array += 1
    if kapal_array != 0 :
        kapal_total += (kapal_array/kapal_array) 
        kapal_array = 0
    elif kapal_array == 0 :
        kapal_total += 0

#output hasil
print("Terdapat", int(kapal_total), "kapal musuh pada peta")