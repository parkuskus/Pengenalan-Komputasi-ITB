#Bermain-main dengan modulo dan div
#Input
x = int(input("Masukkan bilangan 4 digit:  "))

#Inisialisasi awal
Alfa = False
Beta = False

#Pemrosesan
k = x // 1000 #example 1324 --> 1
l = x //100 % 10 #example 1324 --> 13 --> 3
m = x//10 %10 #example 1324 --> 132 --> 2
n = x%10 #example 1324 --> 4

if (k>l>m>n) or (k<l<m<n) :
    Alfa = True
if (x//100)-(x%100)>30 or (x//100)-(x%100)< -30 :
    Beta = True

#Penentuan
if Alfa and Beta :
    print("Gamma")
elif Alfa :
    print("Alfa")
elif  Beta :
    print("Beta")
else : 
    print("Delta")