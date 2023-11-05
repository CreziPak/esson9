from irst_package import alp
# x = int(input('Введи число 1 брат '))
# y = int(input('Введи число 2 брат '))
# r = input('Брат ввели операцию ')
# if r == '+':
#     print(alp.add(x, y))
# elif r == '-':
#     print(alp.dif(x, y))
# elif r == '*':
#     print(alp.mul(x, y))
# elif r == '/':
#     print(alp.div(x, y))
# elif r == '//':
#     print(alp.div1(x, y))
# elif r == '%':
#     print(alp.div2(x, y))

calp = {'+':alp.add,
        '-':alp.dif,
        '*':alp.mul,
        '/':alp.div,
        '//': alp.div1,
        '%': alp.div2,
        }
r = input('Брат введи операцию ')

x = int(input('Введи число 1 брат '))
y = int(input('Введи число 2 брат '))
print((calp[r])(x, y))