#Pemrosesan Array of Integer
r = int(input(f"Masukkan nilai banyak data: "))
A = [0 for i in range(r)]
for i in range(r) :
    A[i] = int(input(f"Masukkan data ke-{i+1}: "))

find = int(input("Masukkan nilai yang ingin dicari: "))
N = int(input("Masukkan nilai N: "))

nilai = 0

for i in range(r) :
    if A[i] == find :
        nilai += 1
        if nilai == N :
            print(f"Nilai {find} ke-{nilai} terletak pada indeks {i}")