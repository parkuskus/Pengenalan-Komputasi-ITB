#Problem habis dibagi
#Input
A =int(input("Masukkan nilai A :"))
B =int(input("Masukkan nilai B :"))
x =int(input("Masukkan nilai x :"))
y =int(input("Masukkan nilai y :"))

#Inisialisasi
nilai = 0

#Pemrosesan nilai input
for i in range (A,B+1) : #batas atas diubah menjadi B+1 dengan asumsi nilai B masuk ke perhitungan
    if i % x == 0 and i % y == 0 : #mengecek apakah bilangan i pada interval(A,B) habis dibagi 2 dan 3
        nilai += i #menjumlahkan semua nilai i yang mungkin

print(f"Jumlah bilangan yang habis dibagi {x} dan {y} adalah {nilai}")


#Faktor Prima
#input
N = int(input("Masukkan N :"))

r = 2
 
for i in range(2,N) :
    if N % i == 0 :
        prima = True
        for j in range (2, i) :
            if i % j == 0 :
                prime = False
        print(i, end= " ") if prima else 0