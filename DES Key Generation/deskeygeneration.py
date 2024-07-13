import numpy as np

def leftshift(s):
    answer = ""
    temp = s[0]
    for i in range(1, 5):
        answer += s[i]
    answer += s[0]
    return answer

pt = input("Plain Text (8 Bit): ")
while len(pt) != 12:
    print("Plain Text is not 8 bits long")
    pt = input("Plain Text (8 Bit): ")

s = ""
for i in range(len(pt)):
    if i == 5 or i == 11:
        continue
    s += pt[i]
pt = s

left = pt[:5]
right = pt[5:]

left = leftshift(left)
right = leftshift(right)

s = left + right

p = [i for i in range(10)]
np.random.shuffle(p)

key = ""
for i in range(10):
    key += s[p[i]]
print (str(key))