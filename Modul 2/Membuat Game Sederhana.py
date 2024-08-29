# Role warrior memiliki HP (Hit Point) : 100 dan ATK : 10,
# role archer memiliki HP : 150 dan ATK : 5 
# role paladin memiliki HP : 100, ATK point : 5, dan dapat meregenarasi HP-nya sebesar 10%

#Input pemain 1
pemain1 = str(input("Masukkan role pemain 1 : "))
HP1 = int(input(f"Masukkan sisa HP {pemain1} (P1) : "))

#Pemeriksaan nilai pemain 1
if pemain1 == "warrior" and HP1>100 : 
    print("HP tidak valid")
    HP1 = int(input(f"Masukkan sisa HP {pemain1} (P1) : "))
elif pemain1 == "paladin" and HP1>100 :
    print("HP tidak valid")
    HP1 = int(input(f"Masukkan sisa HP {pemain1} (P1) : "))
elif pemain1 == "archer" and HP1>150 :
    print("HP tidak valid")
    HP1 = int(input(f"Masukkan sisa HP {pemain1} (P1) : "))


#Input pemain 2
pemain2 = str(input("Masukkan role pemain 2 : "))
HP2 = int(input(f"Masukkan sisa HP {pemain2} (P2) : "))


#Inisialiasi nilai
if pemain1 == "archer" or pemain1 == "paladin" :
    ATK1 = 5
elif pemain1 == "warrior" :
    ATK1 = 10

if pemain2 == "archer" or pemain2 == "paladin" :
    ATK2 = 5
elif pemain2 == "warrior" :
    ATK2 = 10

ronde = 0

#Pemrosesan
while HP1> 0 and HP2>0 :
    if (pemain1== "warrior" and pemain2== "archer") or (pemain1== "archer" and pemain2== "warrior") or(pemain1== "archer" and pemain2== "archer") or (pemain1== "archer" and pemain2== "warrior"): 
        HP1 -= ATK2
        HP2 -= ATK1
        ronde += 1
    elif (pemain1 == "warrior" and pemain2== "paladin") or (pemain1 =="archer" and pemain2=="paladin"):
        HP1 -= ATK2
        HP2 -= ATK1
        ronde += 1
        HP2 += HP2/10
    elif (pemain1== "paladin" and pemain2== "warrior") or (pemain1== "paladin" and pemain2== "archer") :
        HP1 -= ATK2
        HP2 -= ATK1
        ronde += 1
        HP1 += HP1/10
    elif (pemain1== "paladin" and pemain2== "paladin"):
        HP1 -= ATK2
        HP2 -= ATK1
        ronde += 1
        HP1 += HP1/10
        HP2 += HP2/10

#Program Akhir
if HP1>HP2 : 
    print(f"Pemain 1 akan menang dalam {ronde} ronde.")
elif HP1<HP2 : 
    print(f"Pemain 2 akan menang dalam {ronde} ronde.")
else :
    print("Permainan berakhir dengan hasil seri.")