#Fibonaci
#input
N = int(input("Masukkan N :"))

#Inisialisasi
fn1 = 1
fn2 = 2
count = 0

#Proses
while (fn2<N) :
    if (fn2 % 2 == 0) :
        count+= 1
    temp = fn1
    fn1 = fn2
    fn2 += temp

print(count)