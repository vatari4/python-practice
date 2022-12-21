a1 = 1
a2 = 1000
b = ''
c = 0
k = c
while b != '=':
  c = (a1+a2)//2
  if c == k:
    c -= 1
  print(c)
  b=input()
  if b == '>':
    a1 = c
    elif b == '<':
      a2 = c
    elif b =='=':
      print('Угадал')
k=c
