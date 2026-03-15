from gf2_math import extended_gcd_gf2, poly_divmod, poly_mul

def run_test(a, m_poly):
    inv, history = extended_gcd_gf2(a, m_poly)
    
    print(f"\n>>> NGHỊCH ĐẢO CỦA a = {a}")
    print(f"{'-'*55}")
    print(f"{'Step':<5} | {'q (binary)':<12} | {'r (binary)':<12} | {'s (binary)':<12}")
    
    for i, st in enumerate(history):
        print(f"{i:<5} | {bin(st['q']):<12} | {bin(st['r']):<12} | {bin(st['s']):<12}")
    
    print(f"{'-'*55}")
    print(f"KẾT QUẢ Cuối: {inv} (Nhị phân: {bin(inv)})")
    
    # Em check lại cho chắc ạ
    _, check = poly_divmod(poly_mul(a, inv), m_poly)
    print(f"Check (a * a^-1) % m: {'DÚNG' if check == 1 else 'SAI'}")

if __name__ == "__main__":
    M_POLY = 1033 # Tương đương x^10 + x^3 + 1
    test_cases = [523, 1015]
    
    for val in test_cases:
        run_test(val, M_POLY)