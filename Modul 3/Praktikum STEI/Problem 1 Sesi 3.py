#Problem 1 Praktikum 3 - STEI Sesi 3
time = int(input("Masukkan nilai N: "))
array_harga = [0 for i in range(time)]
array_total = [0 for i in range(time-2)]
for i in range(time) :
    array_harga[i] = int(input(f"Masukkan harga jam ke-{i+1}: "))

harga = 0
k = 0


for i in range (0,time-2) :
    harga = array_harga[i] + array_harga[i+1] + array_harga[i+2]
    array_total[i] = harga
    harga = 0

minimal = array_total[0]

for i in range(time-2) :
    minimal = array_total[i] if array_total[i] < minimal else minimal
print(array_total)
print(f"Total harga yang harus dibayar adalah {minimal}.")