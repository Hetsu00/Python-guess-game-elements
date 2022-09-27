import random

def main ():
    """Start a elements guessing game."""
    print("Guess the elements!")

    periodic = [
        "hydrogen",
        "titanium",
        "carbon",
        "nitrogen",
        "silicon",
        "aluminium",
        "gold",
        "copper",
        "sodium",
        "magnesium",
       ]

    x = random.choice(periodic)
    
    guess = None

    
    while x != guess:

          guess =str(input("What elements am i thinking of? "))

          if x == guess:
              print("You guessed {}. Congratulatoins you got it right!".format(guess))
              break
          elif x == "hydrogen":
              print("A kind of a oksigen")
          elif x == "titanium":
               print("It is achemical and can for ultraviolet light filter ")
          elif x == "carbon":
               print("It is used for chemical plants")
          elif x == "nitrogen":
               print("It is a layer of the earth atmosphere")
          elif x == "silicon":
               print("It is not a metal. It is a kind of a kimia")
          elif x == "aluminium":
               print("It can use for wrapping food")
          elif x == "gold":
               print("It can use for jewelry")
          elif x == "copper":
               print("A kind of metal that can made out of coins and ornaments")
          elif x == "sodium":
               print("An alkali metal")
          elif x == "magnesium":
               print("A kind of metal that easy to bend")
          else:
              print("You guessed {}.Opps wrong answer dude.Please try again!".format(guess))
              break
            
main()
          
