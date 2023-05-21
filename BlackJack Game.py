############### Blackjack Project #####################

import random
import os
from art import logo

def clear(): os.system('cls') #on Windows System
clear()

def draw_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
  pick = random.choice(cards)
  return pick

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0  

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You both lose. Game over!"
  
  if user_score == computer_score:
    return "It's a draw."
  elif computer_score == 0:
    return "Computer has BlackJack! You lose!"
  elif user_score == 0:
    return "You have BlackJack! You win!"
  elif computer_score > 21:
    return "Computer Bust! You Win!"
  elif user_score > 21:
    return "Bust! You lose!"
  elif user_score > computer_score:
    return "You Win!"
  else:
    return "You lose."

def game_start():

  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for space in range(2):
    user_cards.append(draw_card())
    computer_cards.append(draw_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards are {user_cards},  Your score is {user_score}.")
    print(f"   Computer draws: {computer_cards[0]}")
  
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Would you like to draw another card. Type 'y' or 'n': ")
      if user_should_deal == "y":
        user_cards.append(draw_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score <17:
    computer_cards.append(draw_card())
    computer_score = calculate_score(computer_cards)
  print(f"    Your final hand is: {user_cards}, Your final score is: {user_score}")
  print(f"    Computers final hand is: {computer_cards}, Computer final score is: {computer_score}")
  print(compare(user_score, computer_score))
      

while input("Would you like to play blackjack? Type 'y' or 'n': ") == "y":
  clear()
  game_start()


