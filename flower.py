print("Iris flower classifier")
print("----------------------")
print()

quit = False

while not quit:
  pt_length = float(input("Enter petal length: "))
  pt_width = float(input("Enter petal width: "))
  
  if pt_length < 2.5:
    print("Iris classification is Setosa")
  elif pt_width < 1.9:
    print("Iris classification is Versicolor")
  else:
    print("Iris classification is Virginica")
  print()  

  input1 = input("Classify another? (y)es or (n)o: ")
  
  if input1 == "n":
    quit = True
  elif input1 == "y":
    continue
  else:
    nstop = True
    while nstop == True:
      print("Please respond with either (y)es or (n)o.")
      print()
      input1 = input("Classify another? (y)es or (n)o: ")
      if input1 != "y":
        quit = True
        nstop = False
      elif input1 != "n":
        nstop = False
