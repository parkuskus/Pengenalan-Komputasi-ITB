### PROBLEM 1 PRAKTIKUM FTMD SESI 1

## input
n = int(input('Masukkan nilai banyak mahasiswa(n): '))
print('Masukkan nilai praktikum: ') 
array_nilai = [list(map(int, input().split())) for i in range(4)]
x = int(input('Masukkan target(x): '))

## inisialisasi awal

# array untuk menyimpan nilai masing-masing mahasiswa
array_rerata = [0.0 for i in range(n)] # Arra
# array untuk menyimpan nilai masing-masing mahasiswa pada setiap praktikum
array_nilai_siswa = [[0 for j in range(4)] for i in range(n)] 
# array untuk menyimpan rerata tiap mahasiswa
array_rerata = [0.0 for i in range(n)] 

# indeks untuk input nilai masing-masing siswa
p = 0
q = 0

# variabel untuk menghitung mahasiswa yang nilainya di atas target(x)
count = 0 


## pemrosesan 

# proses ekstraksi data mentah ke nilai per mahasiswa
for i in range(4) :
    for j in range(n) :
        array_nilai_siswa[p][q]= array_nilai[i][j]
        p += 1
    p = 0
    q+= 1

# proses menghitung rerata dan penghitungan mahasiswa di atas x
for i in range(n) :
    array_rerata[i] = (array_nilai_siswa[i][0]+array_nilai_siswa[i][1]+array_nilai_siswa[i][2]+ array_nilai_siswa[i][3])/4
    if array_rerata[i]>x :
        count +=1
    
## Output
print(f"Terdapat {count} mahasiswa yang mendapatkan rata-rata nilai praktikum di atas {x} ")
    

       