#Prioritas Percabangan 1
GPU = int(input("Nilai GPU : "))
CPU = int(input("Nilai CPU : "))
hardisk = int(input("Nilai hardisk :"))

if(GPU <2) or (CPU<2) or (hardisk<2) :
    print("Kelompok 1") 
elif (GPU <5) or (CPU<5) :
    print("Kelompok 2")
elif (GPU <=7) and (CPU<=7) and (hardisk<=7) :
    print ("Kelompok 3")
elif (GPU <=7) or (CPU<=7) or (hardisk<=7) :
    print("Kelompok 4")
elif (GPU >7) and (CPU>7) and (hardisk>7) :
    print("Kelompok 5")


