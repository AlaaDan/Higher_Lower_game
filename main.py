from art import logo, vs
from game_data import data
from replit import clear
import random
game_over = True


def getting_random_dec():
  '''Returns a random dectionary from the gam_data list'''
  return random.choice(data)


random_a = getting_random_dec()
random_b = getting_random_dec()


def compare():
  '''Compares the user input with the random_a and random_b'''
  
  user_guess = input(f"Who has the most followers? Type 'A' or 'B': ").lower()
  if user_guess == "a":
    if random_a["follower_count"] > random_b["follower_count"]:
      return 1
    elif random_a["follower_count"] == random_b["follower_count"]:
      return 4
    else:
      return 3
  elif user_guess == "b":
    if random_b["follower_count"] > random_a["follower_count"]:
      return 2
    elif random_a["follower_count"] == random_b["follower_count"]:
      return 4
    else:
      return 3
  else:
    return
      

score = 0
while game_over:    
  print(logo)
  if score != 0:
    print(f"You're right! Current score: {score}")
  
  print(f"Compare A:\n{random_a['name']}, a {random_a['description']}, from {random_a['country']}.")
  print(vs)
  print(f"Compare B:\n{random_b['name']}, a {random_b['description']}, from {random_b['country']}.") 
  who_will_change = compare()
  
  if who_will_change == 1:
    score +=1
    random_a = random_b
    random_b = getting_random_dec()
  elif who_will_change == 2:
    score+=1
    random_b = getting_random_dec()
  elif who_will_change == 4:
    random_b = getting_random_dec()
  else:
    game_over = False
   
  clear()
print(logo)
print(f"You were wrong! Final score: {score}")
