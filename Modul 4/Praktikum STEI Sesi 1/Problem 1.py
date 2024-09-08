def diskriminan(p,q,r : int) -> float :
    return float(q*q-4*p*r)

def jenis(p,q,r: int) -> None: 
    print(f'Nilai diskriminan: {diskriminan(a,b,c)}')
    if diskriminan(p,q,r) > 0 :
        return print('Persamaan kuadrat memiliki akar berbeda')
    if diskriminan(p,q,r) == 0 :
        return print('Persamaan kuadrat memiliki akar kembar')
    if diskriminan(p,q,r) < 0 :
        return print('Persamaan kuadrat tidak memiliki akar real')

a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = int(input("Masukkan nilai c: "))

diskriminan(a,b,c)
jenis(a,b,c)