#Pengenalan Fungsi dan Prosedur
def header_nama(nama : str) :
    print(f"Nama pengguna: {nama}")
    print(f"Makanan favorit {nama} adalah: ")

def tampil_makanan(nomor, makanan) :
    print(f"{nomor}. {makanan}")
    
user = input("Masukkan nama pengguna: ")
n = int(input("Masukkan banyaknya makanan favorit: "))
favorites = [input(f"Masukkan makanan favorit ke-{i+1}: ") for i in range(n)]

header_nama(user)
for i in range(n):
    tampil_makanan(i+1, favorites[i])