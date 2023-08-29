import random 
from collections import defaultdict

def presentation():
  message = """
  ----
  ### Cows & Bulls using Python 
  # Welcome to Cows & Bulls, this is a simple guessing game where a secret is generated between
  # the values of 1000 & 9999. Your task is to guess what the secret is!
  # Bull is return if the number if correct and in right place.
  # Cow is return if the number is present in the secret but at the wrong place.
  ###
  ----
"""
  print(message)

def getListOfStrings(digits):
  """
    Extract the digits from defined input and return them as a list of strings
  """
  listOfDigits = []
  for i in str(digits):
    listOfDigits += i;
  return listOfDigits

def checkGuess(secret, guess):
  """
    Check if the guess matches the secret, will verify each individual value
  """
  bullCowMatch = ["","","",""]
  secretList = getListOfStrings(secret)
  guessList = getListOfStrings(guess)

  index = 0
  for secretDigit,guessDigit in zip(secretList, guessList): # pairs each index value from each list as a tuple
    # Check if the single "guess digit" even exist in the secret
    if guessDigit in secretList:
      if guessDigit == secretDigit:
        bullCowMatch[index] = "Bull"
      else:
        bullCowMatch[index] = "Cow"
      #
      index += 1

  return bullCowMatch

def generateTheSecret():
  """
    Randomly make a secret
  """
  generatedSecret = random.randint(1000,9999)
  return generatedSecret

def verifyGuess(guess):
  """
    Check if the guess only contains 4 digits
  """
  if len(guess) == 4 and guess.isdigit():
    return True
  else:
    return False

"""
  Script start
"""
presentation() # print message
secret = 1234 #generateTheSecret()
triesLeft = int(input("Please enter the number of tries you wish to have: "))
while triesLeft > 0:
    guess = input("Please take a guess: ") # leave as string input 
    if verifyGuess(guess) == False:
      print("Whoops, to many digits in your guess, you lost one of your tries for nothing!")
      continue
    bullCowResult = checkGuess(secret, guess)
    print(bullCowResult)
    triesLeft -= 1
    if bullCowResult.count('Bull') == 4:
      print("You win!")
      break
else:
  print("No more tries left, you lost!")
