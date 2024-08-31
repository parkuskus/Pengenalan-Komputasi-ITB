n = int(input())

r = n
akhir = 1
#menghitung faktorial
while r>=1 :
    akhir *= r
    r-= 1


x = str(akhir)
array = [i for i in x]

jumlah = 1
for i in range(len(array)):
    jumlah*= int(array[i])

print(jumlah)