for i in range(2):
    for j in range(3):
        for k in range(4):
            print ('i:',i)
            print ('j:', j)
            print ('k:', k)
print ("%%%%%%%%%")

n = 4
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)