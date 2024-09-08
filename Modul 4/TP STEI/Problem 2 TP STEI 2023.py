#Problem 2 Tugas Pendahuluan Praktikum STEI 2023 (COBA DIBUAT DALAM BENTUK FUNGSI)
#fungsi pertambahan
def tambah_bakteri(r: int) :
    return r*2

#input
N = int(input("Masukkan N : "))
M = int(input("Masukkan M : "))  
array_bakteri_akhir = [0 for i in range(M+1)]
array_bakteri_akhir[0] = N
array_bakteri_pertambahan = [0 for i in range(M+1)]
array_bakteri_pertambahan[0] = N


#pemrosesan
for i in range(1, M+1) :
    array_bakteri_pertambahan[i] = tambah_bakteri(array_bakteri_pertambahan[i-1])
    array_bakteri_akhir[i] = array_bakteri_akhir[i-1] + array_bakteri_pertambahan[i]
    
#output
print(array_bakteri_pertambahan)
print(array_bakteri_akhir)    
print(f"terdapat {array_bakteri_akhir[M]} Bakteri Pengkombacter")