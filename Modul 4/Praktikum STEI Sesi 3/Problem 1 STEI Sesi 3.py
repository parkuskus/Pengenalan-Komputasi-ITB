#Problem 1 Praktikum 4 STEI Sesi 3
def cekvalid(p,q,r) :
    if (0<p<1) and (0<q<1) and (0<q<1) and (p+q+r == 1) :
        return True
    else : 
        return False

def hitung(p,q,r,x1,x2,x3) :
    if cekvalid(p,q,r) == True :
        return print(f'Nilai tugas praktikum adalah {p*x1 + q*x2 + r*x3}')
    else :
        return print("bobot tidak valid")

a  = float(input("Masukkan nilai a: "))
b  = float(input("Masukkan nilai b: "))
c  = float(input("Masukkan nilai c: "))
n1 = int(input("Masukkan nilai soal 1: "))
n2 = int(input("Masukkan nilai soal 2: "))
n3 = int(input("Masukkan nilai soal 3: "))

cekvalid(a,b,c) 
hitung(a,b,c,n1,n2,n3) 