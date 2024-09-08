#Fungsi dan Pengulangan    
#Mencari prima
def isprima(x:int) -> bool :
    prima = True
    if x <= 1 :
        prima = False
    elif x == 2 :
        prima = True
    elif x>2 :
        for i in range(2,x) :
            if x%i == 0 :
                prima = False
    return prima

#Program f(x)
def f(x:int) -> int :
    biggest = 0
    for i in range(2,x+1) :
        if x%i == 0 and isprima(i) :
            if i>biggest :
                biggest = i
    return biggest
#Input
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

jumlah = 0
#Proses
for i in range(m,n+1) :
    jumlah += f(i)
    
#Hasil
print(f"Jumlah faktor prima terbesar untuk m sampai n adalah {jumlah}.")