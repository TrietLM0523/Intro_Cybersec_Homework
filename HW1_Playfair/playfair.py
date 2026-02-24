class PlayfairCipher:
    def __init__(self, key):
        self.matrix = self.create_matrix(key)

    def create_matrix(self, key):
        key = key.upper().replace('J', 'I')
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        combined = ""
        for char in key + alphabet:
            if char.isalpha() and char not in combined:
                combined += char
        return [list(combined[i:i+5]) for i in range(0, 25, 5)]

    def find_position(self, char):
        for r in range(5):
            for c in range(5):
                if self.matrix[r][c] == char:
                    return r, c
        return None

    def prepare_text(self, text):
        text = text.upper().replace('J', 'I').replace(" ", "")
        prepared = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = text[i+1] if (i + 1) < len(text) else 'X'
            
            if a == b:
                prepared += a + 'X'
                i += 1
            else:
                prepared += a + b
                i += 2
        if len(prepared) % 2 != 0:
            prepared += 'X'
        return prepared

    def encrypt(self, plaintext):
        text = self.prepare_text(plaintext)
        result = ""
        for i in range(0, len(text), 2):
            r1, c1 = self.find_position(text[i])
            r2, c2 = self.find_position(text[i+1])

            if r1 == r2: # Cùng hàng
                result += self.matrix[r1][(c1 + 1) % 5] + self.matrix[r2][(c2 + 1) % 5]
            elif c1 == c2: # Cùng cột
                result += self.matrix[(r1 + 1) % 5][c1] + self.matrix[(r2 + 1) % 5][c2]
            else: # Hình chữ nhật
                result += self.matrix[r1][c2] + self.matrix[r2][c1]
        return result