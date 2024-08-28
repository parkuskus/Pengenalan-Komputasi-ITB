#Dasar Percabangan
KoinNay = int(input("Banyak koin Nay : "))
KoinAka = int(input("Banyak koin Aka : "))
NilaiNay = int(input("Nilai Konversi Nay ke rupiah :"))
NilaiAka = int(input("Nilai Konversi Aka ke rupiah :"))

if (KoinNay*NilaiNay > KoinAka*NilaiAka) :
    print("Darrel lebih memilih Koin Nay")
elif (KoinNay*NilaiNay < KoinAka*NilaiAka) :
    print("Darrel lebih memilih Koin Aka")
else :
    print("Tidak dapat disimpulkan")