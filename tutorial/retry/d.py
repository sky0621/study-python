#squares = []
squares = list()
for x in range(10):
#    squares.append(x * x)
    squares.append(x**2)

print(squares)
print(x)

print("="*100)

# ラムダバージョン
squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

print("="*100)

# リスト内包
squares3 = [x**2 for x in range(10)]
print(squares3)

print("="*100)

lislis = [(x, y) for x in range(3) for y in range(4) if x != y]
print(lislis)
