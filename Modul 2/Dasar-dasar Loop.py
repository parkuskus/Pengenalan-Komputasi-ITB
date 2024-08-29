#Dasar For Loop
#Input
N = int(input("Masukkan nilai N :"))

#Inisialisasi
skorN = 0
skorD = 0

#Pemrosesan
for i in range (1,N+1) :
    GerakN = str(input(f"Gerakan Nayaka di ronde {i} adalah : "))
    GerakD = str(input(f"Gerakan Darrel di ronde {i} adalah : "))
    #N = Batu
    if GerakN == "batu" and GerakD == "gunting" :
        skorN += 1
    elif GerakN == "batu" and GerakD == "kertas" :
        skorD += 1
    #N = Kertas
    elif GerakN == "kertas" and GerakD == "gunting" :
        skorD += 1
    elif GerakN == "kertas" and GerakD == "batu" :
        skorN += 1
    #N = Gunting
    elif GerakN == "gunting" and GerakD == "batu" :
        skorD += 1
    elif GerakN == "gunting" and GerakD == "kertas" :
        skorN += 1

if skorD>skorN :
    print(f"Darrel menang dengan skor {skorN}-{skorD}")
elif skorD<skorN :
    print(f"Nayaka menang dengan skor {skorN}-{skorD}")
else : #seri
    print(f"Pertandingan seri dengan skor {skorN}-{skorD}")