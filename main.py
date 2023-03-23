from game_data import data
from art import logo,vs
import random

def compare_followers(firstActor, secondActor):
  if firstActor['follower_count'] > secondActor['follower_count']:
    return firstActor['name']
  else:
    return secondActor['name']

def compare_guess(firstActor, secondActor, userguess):
  if compare_followers(firstActor, secondActor) == userguess:
    return True     
  else:
    return False

def input_user(celeb1,celeb2):
  print(f"A: {celeb1['name']}, a {celeb1['description']}, from {celeb1['country']}")
  print(vs)
  print(f"B: {celeb2['name']} a {celeb2['description']} from {celeb2['country']}")
  userguess = ''
  while userguess not in ('a','b'):
    userguess = input(f"Guess who has more followers. A or B: ").lower()
    
  if userguess == 'a':
    return celeb1['name']
  if userguess == 'b':
    return celeb2['name']
  

#while play_game:
print(f"{logo}")
celeb1 = random.choice(data)
celeb2= random.choice(data)
if celeb1 == celeb2:
  celeb2 = random.choice(data)
score = 0
user_choice = input_user(celeb1,celeb2)

while compare_guess(celeb1, celeb2, user_choice):
  score+= 1
  if user_choice == celeb2['name']:
      celeb1 = celeb2
      celeb2= random.choice(data)
      if celeb1 == celeb1:
        celeb2 = random.choice(data)
  if user_choice == celeb1['name']:
      celeb2 = random.choice(data)
      if celeb1 == celeb2:
        celeb2 = random.choice(data)
  user_choice = input_user(celeb1,celeb2)
  compare_guess(celeb1,celeb2, user_choice)
  
print(f"Wrong..Final Score: {score}")