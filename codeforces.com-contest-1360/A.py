testCases = int(input())

for testCase in range(testCases):
    z = input().split()
    
    if z[0] > z[1]:
        a = int(z[0])
        b = int(z[1])
    else:
        a = int(z[1])
        b = int(z[0])

    if a >= 2*b:
        print(a*a) 
    else:
        print(b*b*4)