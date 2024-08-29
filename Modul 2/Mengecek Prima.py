#Mengecek Prima
#input
N = int(input("Masukkan N :"))

r = 2
Prima = True

while(r<N) :
    if N % r ==0 :
        Prima = False
    r += 1

print(Prima)



#Pola Bilangan
x = int(input("Masukkan x :"))
y = int(input("Masukkan y :"))

#Inisialisasi
count = 0
yi = y

#Proses
while count<x :
    i = 1
    # Barisan naik
    while i<y and count<x :
        print(i, end=" ")
        i += 1
        count += 1
    
    y += yi
    
    # Barisan turun
    while i>1 and count<x :
        print(i, end=" ")
        i -=1
        count +=1