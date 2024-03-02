def cek_digit_belakang(a, b, c):
    kanan1 = a % 10
    kanan2 = b % 10
    kanan3 = c % 10
    
    if kanan1 == kanan2:
        return True
    elif kanan1 == kanan3:
        return True
    elif kanan2 == kanan3:
        return True
    else:
        return False
    
try:
    a = int(input("Masukkan angka a: "))
    b = int(input("Masukkan angka b: "))
    c = int(input("Masukkan angka c: "))
except:
    print("Inputan salah!")
    
print(cek_digit_belakang(a, b, c))