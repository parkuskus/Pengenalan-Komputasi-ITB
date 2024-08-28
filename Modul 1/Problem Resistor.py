#Membuat Resistor
x = int(input("Masukkan hambatan resistor ke-1 :"))
y = int(input("Masukkan hambatan resistor ke-2 :"))
z = int(input("Masukkan hambatan resistor ke-3 :"))

rtot = (x*y*z)/(y*z+x*z+x*y)
if (x<=0) or (y<=0) or (z<=0) :
    print("Hambatan tidak dapat dihitung")
else : #(x>=0) or (y>=0) or (z>=0)
    print(f"Hambatan total rangkaian adalah {rtot} ohm.")