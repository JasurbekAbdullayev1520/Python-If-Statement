a=int(input('a tomonni kiriting'))

b=int(input('b tomonni kiriting'))

c=int(input('c tomonni kiriting'))

if a==b and b==c:
    print('Teng yonli')

if a==b or b==c or c==a:
    print('Teng tomonli')
else:
    print('Turli tomonli')