#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

def tipCalculator():
  print("Welcome to the tip calculator!")
  bill = float(input("What was the total bill? ").replace("$",""))
    
  def getPerc():
    perc = input("What percentage tip would you like to give? 10, 12 or 15? ")
    if perc == "10" or perc == "12" or perc == "15":
      return perc
    else:
      print("You can only choose between 10, 12 or 15 percentage.")
      return getPerc()
     
  perc = float(getPerc())
  
  nPeople = float(input("How many people to split the bill? "))

  dividedBill = bill * (perc/100+1) / nPeople

  print(f"Each person should pay: ${round(dividedBill, 2)}")

  







tipCalculator()
