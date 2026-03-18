def ksa(s_arr, key_arr):
    s = s_arr.copy()
    j = 0
    n = len(s)
    
    for i in range(n):
        j = (j + s[i] + key_arr[i % len(key_arr)]) % n
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        
    return s

def prga(s_arr, length):
    i = 0
    j = 0
    n = len(s_arr)
    k_stream = []
    
    for _ in range(length):
        i = (i + 1) % n
        j = (j + s_arr[i]) % n
        
        tmp = s_arr[i]
        s_arr[i] = s_arr[j]
        s_arr[j] = tmp
        
        t = (s_arr[i] + s_arr[j]) % n
        k_stream.append(s_arr[t])
        
    return k_stream