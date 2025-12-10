def dicti(a):
  
  try:
    print(f"Traamslating Your Words .....\n{a} -----> {dic[a.lower()]}")
  except:
      print("sorry we can't translate Your Words")
dic = {"new":"naya","old":"purana",'dream':'sapna',"true":"sahi",'false':'galat'}
c = input("enter your words ")
print(c)
dicti(c)
