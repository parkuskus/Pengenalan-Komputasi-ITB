#Input
jb = int(input("Jam keberangkatan : "))
jp = int(input("Jam kepulangan : "))

#Proses
buskota = 7<=jb<=18
buskota = 7<=jp=<18
busuniv = 6<=jb<=8
busuniv = 6<=jp<=8
busuniv = 15<=jb<=17
busuniv = 15<=jp<=17
travel = jp>0
travel = jb>0

hbk = 5000
hbg = 0
HT = 10000

print(buskota)