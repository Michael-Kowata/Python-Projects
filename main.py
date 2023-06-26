# import time and random functions to use in the program
import random
import time

# list of pause times and responses
pause=[0, 1, 2, 3, 4, 5, 6]
responses=["It is certain", "It is decidedly so", "Without a doubt",  "Yes definitely", "You may rely on it", "As I see it, yes",  "Most likely",  "Outlook good", "Yes",  "Signs point to yes", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]

question=0
while (question!=1):
  question=input("Ask a question: ")
  if question.upper()=="Q": #If the user enters a "q" or a "Q" for their question, the loop will end 
    print("Thanks for playing!")
    question=1 #makes the while loop false
  else:
    time.sleep(random.choice(pause)) #chooses a random time to pause from the pause list
    print(random.choice(responses)) #chooses a random response from the responses list

