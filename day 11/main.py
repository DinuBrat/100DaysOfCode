import random
from art import logo
import os


def draw_card(hand):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  hand.append(random.choice(cards))

  return hand

def calculate_score(hand):
  score = sum(hand)
  if score > 21:
    for card in hand:
      if card == 11:
        hand.remove(card)
        hand.append(1)
        score = sum(hand)
  return score

def compare(user_score, computer_score):
  if user_score > 21:
    print("You went over. You lose 😤")
  elif computer_score > 21:
    print("Opponent went over. You win 😁")
  elif user_score == computer_score:
    print("Draw 🙃")
  elif user_score == 21:
    print("Win with a Blackjack 😎")
  elif computer_score == 21:
    print("Lose, opponent has Blackjack 😱")
  elif user_score > computer_score:
    print("You win 😃")
  else:
    print("You lose 😤")

def blackjack():
  user_hand = []
  computer_hand = []
  for i in range(2):
    user_hand = draw_card(user_hand)
    computer_hand = draw_card(computer_hand)
  user_score = calculate_score(user_hand)
  computer_score = calculate_score(computer_hand)
  print(f"Your cards: {user_hand}, current score: {user_score}")
  print(f"Computer's first card: {computer_hand[0]}")
  if user_score == 21:
    print("Win with a Blackjack 😎")
  elif computer_score == 21:
    print("Lose, opponent has Blackjack 😱")
  else:
    while user_score < 21:
      draw = input("Type 'y' to get another card, type 'n' to pass: ")
      if draw == "y":
        user_hand = draw_card(user_hand)
        user_score = calculate_score(user_hand)
        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")
      else:
        break
    while computer_score < 17:
      computer_hand = draw_card(computer_hand)
      computer_score = calculate_score(computer_hand)
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    compare(user_score, computer_score)

while input("Do you want to play a game of Blackjack? Yes or No: ") == "Yes":
  os.system('cls||clear')
  print(logo)
  blackjack()


