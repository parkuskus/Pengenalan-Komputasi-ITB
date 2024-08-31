#Pemrosesan String
asli = str(input("Masukkan kata asli : "))
panjang = int(input("Masukkan panjang kata asli : "))
tulis  = str(input("Masukkan kata yang ditulis : "))

x = ""
for i in range(panjang) :
    for j in range(i+1) :
        x+= asli[j]

print(x)

if x == tulis:
    print("Tulisan cucu Mas Hanies sudah benar.")
else:
    print("Tulisan cucu Mas Hanies masih salah.")
