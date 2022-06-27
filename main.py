from art import logo, vs
from game_data import data
import random
game_over = True
def getting_random_dec():
  '''Returns a random dectionary from the gam_data list'''
  return random.choice(data)

random_a = getting_random_dec()
random_b = getting_random_dec()

print(logo)
print(f"Compare A:\n{random_a['name']}, a {random_a['description']}, from {random_a['country']}.")
print(vs)
print(f"Compare B:\n{random_b['name']}, a {random_b['description']}, from {random_b['country']}.")

def compare():
  score = 0
  user_guess = input(f"Who has the most followers? Type 'A' or 'B': ").lower()
  if user_guess == "a":
    if random_a["follower_count"] > random_b["follower_count"]:
      score +=1
      print(f"You're right! Current score: {score}")
      
    else:
      print(f"You are wrong! Final score: {score}")
      return
  else:
    if random_b["follower_count"] > random_a["follower_count"]:
      score +=1
      print(f"You're right! Current score: {score}")
    else:
      print(f"You are wrong! Final score: {score}")
      

 
  
compare()