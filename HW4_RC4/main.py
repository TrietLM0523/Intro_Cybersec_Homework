import rc4

def run_crypto():
    s_vec = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    k_vec = [2, 4, 1, 7]
    msg = "cybersecurity"

    m_t = []
    for c in msg:
        m_t.append(ord(c))

    s_ready = rc4.ksa(s_vec, k_vec)
    
    stream = rc4.prga(s_ready, len(m_t))
    print("Keystream:", stream)
    
    c_t = []
    for i in range(len(m_t)):
        res = m_t[i] ^ stream[i]
        c_t.append(res)

    print("Ciphertext:", c_t)

if __name__ == "__main__":
    run_crypto()
    