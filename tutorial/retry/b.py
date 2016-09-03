print('ABC')

def ask_ok(prompt, retry=4, compl='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes'):
            return True
        if ok in ('n', 'no'):
            return False
        retry = retry - 1
        if retry < 0:
            raise OSError('非協力的なユーザー')
        print(compl)

ask_ok('Prom')
