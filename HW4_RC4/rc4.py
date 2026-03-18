def ksa(s_arr, key_arr):
    s = list(s_arr)
    j = 0
    n = len(s)
    
    for i in range(n):
        j = (j + s[i] + key_arr[i % len(key_arr)]) % n
        s[i], s[j] = s[j], s[i]
        
    return s

def prga(s_arr):

    i, j = 0, 0
    n = len(s_arr)
    
    while True:
        i = (i + 1) % n
        j = (j + s_arr[i]) % n
        
        s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
        
        t = (s_arr[i] + s_arr[j]) % n
        yield s_arr[t]