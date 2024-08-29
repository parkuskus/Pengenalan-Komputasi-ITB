m = int(input())

hitung = 0
count = 0
jarak = m
i = 1
while jarak>0 :
    while 2**i<=jarak :
        i+= 1
    i = i-1
    hitung = 2**i
    jarak = jarak - hitung
    count +=1

print(count)
