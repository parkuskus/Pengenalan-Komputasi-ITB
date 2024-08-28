b = int(input()) 
n = int(input())
p = int(input()) 

bayar = 0

if 0<=b<10**4 and 1<=p<=100 :
    if 1<=p<=4 :
        if n == 0 :
            bayar = 0.9*p*25
        elif n == 1 :
            bayar = 0.9*p*100
    elif 5<=p<=10 :
        if n == 0 :
            bayar = 0.85*p*25
        elif n == 1 :
            bayar = 0.85*p*100
    elif 11<=p<=20 :
        if n == 0 :
            bayar = 0.80*p*25
        elif n == 1 :
            bayar = 0.80*p*100
    elif 21<=p<=30 :
        if n == 0 :
            bayar = 0.75*p*25
        elif n == 1 :
            bayar = 0.75*p*100
    elif p>30 :
        if n == 0 :
            bayar = 0.70*p*25
        elif n == 1 :
            bayar = 0.70*p*100

if bayar>b :
    print('TIDAK')
    print(format(bayar-b,".2f"))
else :
    print('YA')
    print(format(b-bayar,".2f"))