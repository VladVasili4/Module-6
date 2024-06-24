
pass_word = input('Введи пароль')
abc_ = []
# a = 0
# b = 0
# c = 0
def password(pass_word):
    global abc_
    if len(pass_word) > 8:
        a = '0'
        b = 0
        c = 0
        for i in range(0, len(pass_word)):
            sign = pass_word[i]
            if sign.isdigit():
                a = 1
                print('a', a)
                print(abc_)
            else: d = 0
            if sign.islower():
                b = 1
                print('b', b)
            else: d = 0
            if sign.isupper():
                c = 1
                print('c', c)
            else:
                d = 0
            print(f'sign = {sign}')
        abc_ = [a, b, c]

        print(f'abc_ {abc_}')
    else:
        print('Пароль слишком короткий')
    if abc_ == [1, 1, 1]:
        print (f'{pass_word} хороший пароль')
    else:
        print('Пароль не соответствует уровню сложности')

password(pass_word)







# foo = (bool(len(pass_word) > 9)),
#        any(map(lambda x: x.isdigit(), data)),
#        any(map(lambda x: x.islower(), data)),
#        any(map(lambda x: x.isupper(), data))
# return all(foo)

