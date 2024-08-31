#Pemrosesan Array of String
#SOLUSI AUFAR 
length  = int(input("Panjang pesan : "))
message = str(input("Pesan : "))
special = str(input("Karakter pengganti spasi : "))

A = [message[i] for i in range(length)]

for i in range(length) :
    if A[i] == special :
        A[i] = " "

for i in range(length) :
    print(A[i], end="")
    
#Solusi 1
n = int(input("Panjang pesan: "))
pesan = input("Pesan: ")
k = input("Karakter pengganti spasi: ")

for i in range(n):
    print(" ", end="") if pesan[i] == k else print(pesan[i], end="")

#Solusi 2 
#Input
lenght = int(input("Panjang pesan :"))
pesan = str(input("Pesan : "))
pengganti = str(input("Karakter pengganti spasi : "))

#Inisialisasi
array = [pesan[i] for i in range(lenght)]
for i in range(lenght) :
    if array[i] == pengganti :
        array[i] = " "
print("")
print("Pesan : ", end="")
for i in range(lenght) :
    print(array[i], end="")