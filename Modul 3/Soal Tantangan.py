def perlu_remedial(nilai_uts):
    if nilai_uts<70 :
        return True
    else : 
        return False

# Contoh Kasus
print(perlu_remedial(75))  # Output: False
print(perlu_remedial(65))  # Output: True