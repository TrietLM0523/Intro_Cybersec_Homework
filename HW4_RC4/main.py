import rc4

def main():
    s_vec = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    k_vec = [2, 4, 1, 7]
    msg = "Cybersecurity"

    m_t = [ord(c) for c in msg]

    s_ready = rc4.ksa(s_vec, k_vec)
    
    key_stream_gen = rc4.prga(s_ready)
    
    stream_used = []
    c_t = []
    
    for byte in m_t:
        k = next(key_stream_gen)
        stream_used.append(k)
        c_t.append(byte ^ k)

    print("Keystream:", stream_used)
    print("Ciphertext:", c_t)

if __name__ == "__main__":
    main()