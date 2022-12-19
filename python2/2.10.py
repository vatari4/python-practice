firstStr = float(input("Введите число"))      #1 строка
secondStr = float(input("Введите число"))     #2 строка
thirdStr = str(input("Введите строку"))       #3 строка
if "-" in thirdStr:                  #если в строке встречается "-" то из 1 строки 
  firstStr -= secondStr
  print(firstStr)
elif("+" in thirdStr):
  firstStr += secondStr
  print(firstStr)
elif("*" in thirdStr):
  firstStr *= secondStr
  print(firstStr)
elif("/" in thirdStr):
  firstStr /= secondStr
  print(firstStr)
else:
  print("888888888")
