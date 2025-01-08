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
game_img=[rock,paper,scissors]
a=int(input("Enter the 0,1,2 for rock,paper,scissors:"))
if a==0 or a==1 or a==2:
    print(game_img[a])
    random_c=random.randint(0,2)
    print("Compute choose:",random_c)
    print(game_img[random_c])
    if a>=3 or a<0:
        print("Select a proper number!")
    elif a==0 and random_c == 2:
        print("You win!!!")
    elif a==2 and random_c==0:
        print("You Loose.")
    elif random_c>a:
        print("You Loose.")
    elif random_c<a:
        print("You Win!!!")
    elif random_c==a:
        print("Draw")
else:
    print("Select proper number!!!")
