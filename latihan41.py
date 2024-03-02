def cek_angka(a, b, c):
    if (a!=b and a!=c and b!=c)and(a+b==c or b+c==a or c+a==b):
        return True
    else:
        return False
    
print("Test-Case: ")
print(f"(2, 3, 6){cek_angka(2, 3, 6)}")
print(f"(2, 3, 5){cek_angka(2, 3, 5)}")



