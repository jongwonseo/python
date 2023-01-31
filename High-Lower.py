from art import logo
from art import vs
from game_data import data
import random

def format_data(account):
  """Format the account datat into printable format."""
  
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"
  
def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and return if they got it right."""
  if a_follower_count > b_follower_count:
    return guess =="a"
  else:
    return guess == 'b'


# Display art
print(logo)
score = 0
game_should_continue = True 
account_b = random.choice(data)

while game_should_continue:

  # Generate a random account from the game data
  account_a = account_b
  account_b = random.choice(data)
  
  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  # Ask user form a guess.
  guess = input("Who has more followers? A, B:     ").lower()



  # Cehck if user is correct.
  ## Get floower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Give user feedback on their guess.
  if is_correct:
    score += 1
    print(f"right!, score:{score}")
  else:
    game_should_continue = False
    print(f"wrong,  score:{score}")
# Score keeping.

# Make the game repeatable.

# Making account at position B become the next account at position A.

# Clear the screen between 