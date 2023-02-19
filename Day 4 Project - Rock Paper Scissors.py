import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
imgs = [rock, paper, scissors]
options = ["rock", "paper", "scissors"]
compPlay = random.randint(0,2)

pPlay = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if pPlay == compPlay:
    print(f"{imgs[pPlay]}\nComputer Chose:\n{imgs[compPlay]}\nYou tied")
elif pPlay == 0 and compPlay == 1:
    print(f"{imgs[pPlay]}\nComputer Chose:\n{imgs[compPlay]}\nYou lose")
elif pPlay == 0 and compPlay == 2:
    print(f"{imgs[pPlay]}\nComputer Chose:\n{imgs[compPlay]}\nYou win")
elif pPlay == 1 and compPlay == 0:
    print(f"{imgs[pPlay]}\nComputer Chose:\n{imgs[compPlay]}\nYou win")
elif pPlay == 1 and compPlay == 2:
    print(f"{imgs[pPlay]}\nComputer Chose:\n{imgs[compPlay]}\nYou lose")
elif pPlay == 2 and compPlay == 0:
    print(f"{imgs[pPlay]}\nComputer Chose:\n{imgs[compPlay]}\nYou lose")
elif pPlay == 2 and compPlay == 1:
    print(f"{imgs[pPlay]}\nComputer Chose:\n{imgs[compPlay]}\nYou Win")

