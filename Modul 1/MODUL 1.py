#program ganjil genap
print("Masukkan nilai N : ", end="")
N = int(input())

if  (N>0 and N%2 == 0 ) : 
    print(str (N), "adalah bilangan positif genap")
elif (N<0) : 
    print(str(N), "adalah bilangan negatif. tidak bisa ditentukan")
elif (N>0 and N%2 != 0) :
    print (str(N), "adalah bilangan positif ganjil")


#Perkalian Sederhana
print("Program ini akan mengalikan angka yang masukkan dengan 5")
N = int(input("masukan sebuah angka : "))
print("hasil operasinya adalah", str(N * 5))