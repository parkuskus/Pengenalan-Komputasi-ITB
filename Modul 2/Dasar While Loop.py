#Dasar While Loop
#Input
h = float(input("Ketinggian awal hola (h) :"))
x = int(input("Nilai x :"))

#Inisialisasi
pantulan = 0

#Pemrosesan 
if x == 1 :
    print("program tidak dapat dijalankan")
else : 
    while (h>=1) : 
        h/=x
        pantulan += 1

    print(f"Terjadi {pantulan} pantulan.")  