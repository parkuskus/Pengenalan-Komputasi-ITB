#Prioritas Percabangan 2
J1 = int(input("Jam keberangkatan :"))
J2 = int(input("Jam pulang :"))

biaya = 0

#Berangkat
if (6<=J1<=8) or (15<=J1<=17) :
    biaya += 0
    transportasi1 = "Bus Universitas"
elif (7<=J1<=18) :
    biaya += 5000
    transportasi1 = "Bus Kota"
else :
    biaya += 10000
    transportasi1 = "travel"

#Pulang
if (6<=J2<=8) or (15<=J2<=17) :
    biaya += 0
    transportasi2 = "Bus Universitas"
elif (7<=J1<=18) :
    biaya += 5000
    transportasi2 = "Bus Kota"
else :
    biaya += 10000
    transportasi2 = "travel"

print(f"Mas Hanies berangkat naik {transportasi1} dan pulang naik {transportasi2} dengan biaya {biaya}")