def f(a, L=[]):
    L.append(a)
    return L


# L=[] のデフォルト値が共有される
print(f(1))
print(f(2))
print(f(3))

print('----------')

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2))
print(f2(3))

print('=' * 70)
print('=' * 70)

def color(now, fine='red', cool='blue'):
    print('now: ' + now, end=', ')
    print('fine: '+ fine, end=', ')
    print('cool: '+ cool, end=', ')
    print()

color('yellow')
color('white', fine='orange')
color('green', cool='black')
color('purple', 'gold')
color('silver', '-', 'brown')

print('=' * 70)
print('=' * 70)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    for arg in arguments:
        print(arg)
    print('-' * 40)

    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger",
           "It's very runny, sir.", "It's really very, VERY runny, sir.",
           shopkeeper="Michael Plain", client="John Cleese", sketch="Cheese Shop Sketch")

