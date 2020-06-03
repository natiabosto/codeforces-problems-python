a = input()
b = input()

n = 0
z = 0

for i in b:
    if i == "n":
        n += 1
    if i == "z":
        z += 1

res = ""

while n:
    res += "1 "
    n-=1

while z:
    res += "0 "
    z-=1

print(res)
