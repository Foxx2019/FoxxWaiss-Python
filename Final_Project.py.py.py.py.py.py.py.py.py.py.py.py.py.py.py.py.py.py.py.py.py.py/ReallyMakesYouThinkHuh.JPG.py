from random import *


player1name = input("Player 1, what's your name?\n: ")
print ("Hello " + player1name +"!")
player2name = input("Player 2, what's your name?\n: ")
print ("Hello " + player2name +"!")


while 1 == 1:
  player1 = input(player1name + ": Roll!")
  x = randint(1,6)
  y = randint(1,6)
  z = randint(1,6)
  a = str(x)
  b = str(y)
  c = str(z)
  print (player1name + " rolled the following: " + a + " " + b + " " + c)
  player1Score = x + y + z
  p1score = str(player1Score)
  print (player1name + "'s score is: " + p1score)
  pause = input(" ")
  player2 = input(player2name + ": Roll!")
  x = randint(1,6)
  y = randint(1,6)
  z = randint(1,6)
  a = str(x)
  b = str(y)
  c = str(z)
  print (player2name + " rolled the following: " + a + " " + b + " " + c)
  player2Score = x + y + z
  p2score = str(player2Score)
  print (player2name + "'s score is: " + p2score)
  pause = input(" ")
  if player1Score > player2Score:
    print (player1name + "'s score of " + p1score + " is greater than " + player2name + "'s score of " + p2score)
    print (player1name + " wins!")
  elif player2Score > player1Score:
    print (player2name + "'s score of " + p2score + " is greater than " + player1name + "'s score of " + p1score)
    print (player2name + " wins!")
  elif player1Score == player2Score:
    print (player1name + "'s score of " + p1score + " is equal to " + player2name + "'s score of " + p2score)
    print ("It's a tie!")
  pause = input(" ")
