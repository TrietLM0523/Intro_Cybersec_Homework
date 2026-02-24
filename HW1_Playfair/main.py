from playfair import PlayfairCipher

def main():
    key = input("Nhập khóa (Key): ")
    cipher = PlayfairCipher(key)
    
    print("\nMa trận 5x5 hiện tại:")
    for row in cipher.matrix:
        print(" ".join(row))
        
    text = input("\nNhập văn bản cần mã hóa: ")
    encrypted = cipher.encrypt(text)
    print(f"Kết quả mã hóa: {encrypted}")

if __name__ == "__main__":
    main()