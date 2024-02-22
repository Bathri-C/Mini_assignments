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


choice=[rock, paper, scissors]
user_num=int(input("What do you choose? Type 0 for Rock,1 for Paper,2 for Scissor: "))
user_choice=choice[user_num]
print("user_choice : ")
print(user_choice)
computer_num=random.randint(0,2)
computer_choice=choice[computer_num]
print("computer_choice : ")
print(computer_choice)
if user_choice==computer_choice:
    print("Match Drawn.")
elif user_num==0 and computer_num==2:
    print("You Win.")
elif user_num==2 and computer_num==0:
    print("Computer Wins.")
elif user_num>computer_num:
    print("You Win.")
else:
    print("Computer Wins.")





