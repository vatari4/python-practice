e = True            #евразия
o = False           #остазия
n = int(input())
for i in range(n):    #переборка i в диапозоне от 0 до n-1
   war = input()
   if war == 'С кем война?':        #если если пользователь введет ... выведет с кем война
       if e:
           print('Евразия')
       else:
           print('Остазия')
   elif war == 'С кем мир?':
       if not o:
           print('Остазия')
       else:
           print('Евразия')
   elif war == 'Менять':                                  #если пользователь введет Менять меняет...
       e, o = o, e
   else:
      print('Error')
       
