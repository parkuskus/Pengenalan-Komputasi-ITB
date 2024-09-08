#Problem 1 Tugas Pendahuluan Praktikum STEI 2023 
#Input
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

A = [list(map(int,input().split())) for i in range(n)]
#alternatif lain untuk input matriks A adalah --> A = [[int(input(f"Masukkan elemen matriks baris {i+1} kolom {j+1}: "))for j in range(n)] for i in range(m)]


#Pemrosesan
biggest = 0 #variabel untuk menentukan nilai terbesar pada sebuah matriks
sementara = 0 #variabel untuk menentukan nilai total sebuah submatriks
for i in range(m-1) :
    for j in range(n-1) : 
        sementara =  A[i][j] + A[i][j+1] + A[i+1][j] +A[i+1][j+1] #mengitung nilai elemen dari sebuah matriks 2x2
        if (sementara > biggest) and (A[i][j]% 2 != 0 or A[i][j+1] % 2 != 0 or A[i+1][j] % 2 != 0 or A[i+1][j+1] % 2 != 0) :
            biggest = sementara #kalo nilai matriks 2x2 (sementara) lebih besar dari nilai terbesar (biggest), maka dia menjadi nilai terbesar

#Output
if biggest == 0 : 
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")  
else :           
    print(f"jumlah maksimum dari submatriks 2x2 yang memiliki elemen ganjil adalah {biggest}")