def fib(n):
    """
    フィボナッチ
    :param n:
    :return:
    """

    a, b = 0, 1
    while a < n:
        print(a, end=',')
        a, b = b, a + b
    print()

fib(2000)


def some(x):
    x = 'update'

y = 'insert'
print(y)
some(y)
print(y)

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib2(100)
print(f100)

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print('Thanks!')
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            print('My God!!')
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('非協力的ユーザー')
        print(complaint)

# prompt only
ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
