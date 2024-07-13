def xor(s1, s2):
    answer = ""
    for i in range(4):
        if s1[i] == s2[i]:
            answer += "0"
        else:
            answer += "1"
    return answer

pt = input("Plain Text (8 Bit): ")
while len(pt) != 8:
    print("Plain Text is not 8 bits long")
    pt = input("Plain Text (8 Bit): ")

key = input("Key (4 Bit): ")
while len(key) != 4:
    print("Key is not 4 bits long")
    pt = input("Key (4 Bit): ")

left = pt[:4]
right = pt[4:]

right = xor(right, key)
left = xor(left, right)

temp = left
left = right
right = temp

ct = left + right
print(ct)