list1 = set()
list2 = set()
words = input()
while words != '':
   list1.add(words)
   words = input()
list1.add(words)
words1 = input()
while words1 != '':
   list2.add(words1)
   words1 = input()
intersection = list1 & list2
if not intersection:
   print('EMPTY')
else:
   for i in intersection:
       print(i)

