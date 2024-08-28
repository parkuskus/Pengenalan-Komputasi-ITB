#Soal Tentang Pengulangan Level Tinggi (Nguli)
#Input
bakso = int(input("Bakso :"))
siomay = int(input("Siomay :"))

#Target akhir : mencari banyaknya seblak yang dapat digunakan dengan ketentuan
#prioritas : Maxwin - Gacor - Mini
#Masing - masing harus ada 1

#ketentuan :
#Seblak Mini : 5 Bakso, 3 Siomay
#Seblak Gacor : 7 Bakso, 5 Siomay
# Seblak MaxWin : 10 Bakso, 7 Siomay


#Memastikan bahwa bisa produksi minimal masing-masing 1 jenis
bakso -= 22
siomay -= 15

#Inisialisasi
mini = 0
gacor = 0
maxwin = 0

#Pemrosesan
if (bakso <= 0) or (siomay <= 0) :
    print("Tidak dapat membuat bakso")

else : 
    mini = 1
    gacor = 1
    maxwin = 1

    if bakso>= 10 and siomay >= 7 :
        if bakso//10 < siomay//7 :
            n = bakso//10
            maxwin += n
            bakso -= 10*n
            siomay -= 7*n
        else : 
            n = siomay // 7
            maxwin += n
            bakso -= 10*n
            siomay -= 7*n

#Gacor
    if bakso>= 7 and siomay >= 5 :
        if bakso//7 < siomay //5 :
            n = bakso//7
            gacor += n
            bakso -= 7*n
            siomay -= 5*n
        if bakso//7 > siomay//5 :
            n = siomay // 5
            gacor += n
            bakso -= 7*n
            siomay -= 5*n

#Mini
    if bakso>= 5 and siomay >= 3 :
        if bakso//5 < siomay //3 :
            n = bakso//5
            mini += n
            bakso -= 5*n
            siomay -= 3*n
        if bakso//5 > siomay//3 :
            n = siomay // 3
            gacor += n
            bakso -= 5*n
            siomay -= 3*n

    print(f"Aufar membuat {mini} porsi seblak mini, {gacor} porsi seblak gacor, {maxwin} porsi seblak maxwin.")