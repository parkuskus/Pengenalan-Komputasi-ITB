#Bermain-main dengan Array
#Solusi AUFAR
elemen = int(input("Masukkan banyaknya elemen: "))
A = [0 for i in range(elemen)]

for i in range(elemen) :
    A[i] = int(input(f"Masukkan bilangan ke-{i+1}: "))

print("Kondisi Awal: ", end=" ")
print(A)    


#Elemen ke-0 yang punya akhir saja
if A[0]>A[1] :
    A[0] = A[0]
elif A[1]>A[0] :
    A[0] = A[1]
    
#Elemen ke-(elemen-1) yang punya awal saja
if A[elemen-1]>A[elemen-2] :
    A[elemen-1] = A[elemen-1]
elif A[elemen-2]>A[elemen-1] :
     A[elemen-1] = A[elemen-2]

#Elemen ke-i yang punya awal dan akhir
for i in range(1,elemen-1) :
    if A[i]>A[i+1] and A[i]>A[i-1] :
        A[i] = A[i]
    elif A[i-1]>A[i+1] and A[i-1]>A[i+1] :
        A[i] = A[i-1]
    elif A[i+1]>A[i] and A[i+1]>A[i-1] :
        A[i] = A[i+1]
    
     
print("Kondisi Akhir: ", end=" ")
print(A)    

#CATATAN : Kode ini rawan salah karena tidak dibuat array baru. Ketika pemrosesan terjadi array awal sudah berubah. Sehingga proses komparasi dapat salah. Namun, pada test case kode ini bekerja. Baiknya dibuat array kosong baru, kemudian diisi lewat proses komparasi tersebut.

#Solusi TUBAY
n = int(input('Masukkan banyaknya elemen : '))
A = [0 for i in range(n)]
for i in range(n) :
    A[i] = int(input(f'Masukkan bilangan ke-{i+1} : ')) 

B = [0 for i in range(n)]

for i in range(n) :
    if i == 0 :
        if A[i]>A[i+1] :
            B[i] = A[i]
        else :
            B[i] = A[i+1]
    elif i == n-1 :
        if A[i]>A[i-1] :
            B[i] = A[i]
        else :
            B[i] = A[i-1]
    else :
        if A[i]>A[i-1] and A[i]>A[i+1] :
            B[i] = A[i] 
        elif A[i-1]>A[i] and A[i-1]>A[i+1] :
            B[i] = A[i-1]
        elif A[i+1]>A[i] and A[i+1]> A[i-1] :
            B[i] = A[i+1]

print('Kondisi awal :', A)
print('Kondisi akhir', B)
