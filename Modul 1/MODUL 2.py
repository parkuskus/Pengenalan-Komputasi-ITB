#MODUL PENGULANGAN 

#LATIHAN 2 (Segitiga Angka)
n = int(input("Masukkan N :"))
for i in range (n+1) :
    for j in range(1, i+1) :
        print(j," ",end="", sep="")
    print()
    
#LATIHAN 1 (Kelipatan 10 terkecil)
n = int(input("Masukkan N: "))
x = 0
while (n > 10**x) :
   x += 1
print(10**x)

#1. Menggunakan sintaks while loop
r = int(input("masukkan angka r = "))
for i in range(1) :
    print (10**r, end="")

#Berikut adalah program yang menerima a dan b dan menuliskan a, a + 1, a + 2, . . . , b − 1, b.
print("----------------------------------")
print("masukkan angka a dan b, dengan (a,b)∈ ℤ dan b>=a" )
a = int(input("a = "))
b = int(input("b = "))
i = a
while (i<=b) :
    print(i)
    i+=1
print("----------------------------------" )

#2. Menggunakan sintaks for loop
a = int(input())
b = int(input())
for i in range(a, b+1):
    print(i)

print("----------------------------------" )

#3. Pengulangan Bersarang (Pengulangan yang di dalamnya ada pengulangan)
n = int(input("Masukkan berapa kali pengulangan yang anda inginkan : "))
for i in range(n) :
    for j in range(n) : 
        print("R", end="")
    print()