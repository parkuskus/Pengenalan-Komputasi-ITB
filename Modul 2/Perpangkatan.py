n = int(input("Masukkan nilai N: "))
k = int(input("Masukkan nilai k: "))

n_awal = n 

status = True
while n>0 and status==True :
    if n%2 == 0 :
        n = n/2
    else :
        status = False

if status== True :
    print(f"{n_awal} merupakan perpangkatan {k}.")
else :
    print(f"{n_awal} bukan merupakan perpangkatan {k}.")
