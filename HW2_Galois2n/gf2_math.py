def get_degree(n):
    return n.bit_length() - 1

def poly_divmod(a, b):
    if b == 0: return None
    q = 0
    r = a
    deg_b = get_degree(b)
    while get_degree(r) >= deg_b:
        shift = get_degree(r) - deg_b
        q ^= (1 << shift)
        r ^= (b << shift)
    return q, r

def poly_mul(a, b):
    res = 0
    for i in range(b.bit_length()):
        if (b >> i) & 1:
            res ^= (a << i)
    return res

def extended_gcd_gf2(a, m):
    old_r, r = m, a
    old_s, s = 0, 1
    steps = []
    while r != 0:
        q, rem = poly_divmod(old_r, r)
        steps.append({'q': q, 'r': r, 's': s})
        old_r, r = r, rem
        old_s, s = s, old_s ^ poly_mul(q, s)
    return old_s, steps