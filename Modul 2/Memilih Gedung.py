#gedung A : peserta < n, maks 5 kegiatan
#gedung B : sisanya, maks 3 kegiatan
#gedung B penuh, tidak ada kegiatan lagi
#gedung A penuh, isi gedung B


n = int(input("Masukkan nilai N : "))

KgedungA = 0
KgedungB = 0
i= 0
while KgedungB < 3 :
    print(KgedungA, KgedungB)
    i += 1
    peserta = int(input(f"Masukkan peserta kegiatan ke-{i} : "))
    if peserta<n and KgedungA <5  :
        KgedungA += 1
    else : #peserta >=n 
        KgedungB += 1

print(f"Terdapat {KgedungA} kegiatan di gedung A dan {KgedungB} kegiatan di gedung B.")
