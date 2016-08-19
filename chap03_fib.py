a, b = 0, 1
print(a)
while (b < 50):
    print(b)
    a, b = b, a + b

i = 256 * 256
print('The value of i is', i)

c, d = 0, 1
print(c, end=',')
while (d < 500):
    print(d, end=',')
    c, d = d, c + d
