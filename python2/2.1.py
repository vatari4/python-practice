firstCity = input("Выберете город в котором Женя будет в Июле")
secondCity = input("Выберете город в котором Женя будет в Июле")
if(firstCity == "Пенза" and secondCity == "Тула")or(firstCity == "Тула" and secondCity == "Пенза"):
  print("No")
elif(firstCity == "Пенза" and secondCity != "Пенза")or(firstCity == "Тула" and secondCity != "Тула"):
  print("yes")
