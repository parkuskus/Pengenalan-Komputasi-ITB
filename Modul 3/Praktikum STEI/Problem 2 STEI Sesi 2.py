#Probel 2 Praktikum 3 - STEI Sesi 2 (BELUM SELESAI)
banyak_petak = int(input("Masukkan nilai N: "))
array_petak = [0 for i in range(banyak_petak)]
array_nilai = [0 for i in range(banyak_petak)]

for i in range(banyak_petak) :
    array_petak[i] = int(input(f"Tinggi petak ke-{i+1}: "))

skor = 0

print(array_petak)

for i in range(banyak_petak):
    for j in range(i-1,-1) :
        if array_petak[i]>array_petak[j] and skor != j-i  :
            skor += 1
        elif array_petak[i]<=array_petak[j] :
            array_nilai[i] = skor
            skor = 0
            
print(array_nilai)