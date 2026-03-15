from gf2_math import extended_gcd_gf2, poly_divmod, poly_mul

def main():
    # m(x) = x^10 + x^3 + 1
    m_poly = 1033 
    test_case = [523, 1015]
    
    print("--- BAI TAP AN TOAN THONG TIN - HW2 ---")
    print(f"Da thuc m(x) dang so: {m_poly}")
    
    for a in test_case:
        print("\n" + "*"*30)
        print(f"Dang tinh nghich dao cho a = {a}")
        
        ket_qua, cac_buoc = extended_gcd_gf2(a, m_poly)
        
        for i, buoc in enumerate(cac_buoc):
            print(f"Buoc {i+1}:")
            print(f"  + Thuong q = {bin(buoc['q'])}")
            print(f"  + So du r  = {bin(buoc['r'])}")
            print(f"  + He so x  = {bin(buoc['x'])}") # In ra chu x
            print("-" * 20)
            
        print(f"==> Ket qua cuoi cung (x): {ket_qua}")
        print(f"Chuyen sang nhi phan: {bin(ket_qua)}")
        
        # Kiem tra lai
        _, du = poly_divmod(poly_mul(a, ket_qua), m_poly)
        print(f"Check lai (a * x) mod m = {du}")
        if du == 1:
            print("Ket qua dung roi nhe!")
        else:
            print("Co gi do sai sai...")

if __name__ == "__main__":
    main()