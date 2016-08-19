squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
print(x)

squares2 = list(map(lambda y: y**2, range(10)))
print(squares2)
# print(y)

squares3 = [z**2 for z in range(10)]
print(squares3)
# print(z)
