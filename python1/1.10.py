firstStep = input("Bы находитесь в пещере на развилке. Вы можете пойти налево, направо или прямо.")       #первый выбор
if(firstStep == "налево"):
  print("Вы направились налево. Через некоторое время вы дошли до двух дверей.")
elif(firstStep == "направо"):
  print("Дверь заперта")
else:
  print("Дверь заперта")
secondStep = input()      #второй выбор
if(secondStep == "правая"):
  print("Bы смело открыли правую дверь. Но за ней вас подстерегала гигантская подземная жаба")
elif(secondStep == "левая"):
  print("дверь заперта")
else:
  print("Error")
