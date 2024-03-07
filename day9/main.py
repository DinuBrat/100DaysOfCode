import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
bids = {}
print(logo)
print("Welcome to the secret auction program.")
def add_bid(name, bid):
  bids[name] = bid

def get_winner():
  highest_bid = 0
  highest_bidder = ""
  for bidder,value in bids.items():
    if value > highest_bid:
      highest_bid = value
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

while True:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  add_bid(name, bid)
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if other_bidders == "yes":
    os.system('cls||clear')
  else:
    get_winner()
    break
  