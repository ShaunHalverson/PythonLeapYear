def isLeapYear(year):
  if(year % 100 != 0 and year % 4 == 0):
    return True
  elif(year % 100 == 0 and year % 400 == 0):
    return True
  else:
    return False

### User validation loo
while True:
  try:
    currentYear = int(input("Please enter a year: "))
    if(isLeapYear(currentYear)):
      print(currentYear, " is a valid leap year 🐸")
    else:
      print(currentYear, " is not a valid leap year ❌")
  except:
    print("Please try again.")
