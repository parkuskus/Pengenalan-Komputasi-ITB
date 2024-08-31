n = int(input())
akhir = 3
x = 1
r = 1
akhir_mutlak = int(3+((n-1)/2)*(4+((n-2))))
#baris satu
print('*')

#baris naik
for i in range(n) :
    for j in range(akhir) :
        if 0<=j<x :
            print(' ', end='')
        else :
            print('*', end='')     
    print()
    x += r
    r+=1
    akhir += r


f= n
z = r
akhir = akhir - z
print(akhir)
r-=2
print(r)
#baris bawah
for i in range(n+1,2*n+1) :
    akhir = akhir_mutlak - f
    x -= r 
    for j in range(akhir) :
        if 0<=j<x :
            print(' ', end='')
        else :
            print('*', end='')
    r -= 1
    f-= 1     
    print()


