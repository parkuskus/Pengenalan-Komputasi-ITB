#Problem 1 Praktikum 3 - STEI Sesi 2
#Input data yang diperlukan
plat = input("Masukkan nomor plat mobil: ")
sum = int(input("Masukkan jumlah digit: "))
count = int(input("Masukkan banyak digit: "))

#Set data awal
array_plat = [plat[i] for i in range(len(plat))]
array_number = [0 for i in range(count)] #Nanti akan diisi dengan angka pada plat nomor
j = 0 #digunakan sebagai indeks pada saat mengakses array_number
total = 0 #digunakan untuk menghitung jumlah angka pada plat nomor


# "Memindahkan" angka pada plat nomor(array_plat) ke array baru(array_number)
for i in range(1,count+1) :  
    array_number[j] = int(array_plat[i])     
    j += 1

# Menjumlahkan angka pada array_number untuk menghasilkan total angka pada plat nomor 
for i in range(count) :
    total += array_number[i]
    
#Penentuan apakah benar atau tidak    
if array_plat[0] == "D" and total == sum :
    print("Mobil Tuan Kil ditemukan!")
else :
    print("Bukan mobil tuan Kil!")