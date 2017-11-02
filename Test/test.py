#print "Hello World! "*5

"""多行注释符号--用三个引号
import random
secret=random.randint(1,100)
print "The secret number was", secret
guess=0
tries=0
print "I am wzw ,and I have a secret!"
print "It is s number from 1 to 99. I will give you 6 tries."

while guess!=secret and tries<6:
    guess=input("What is your guess?")
    if guess<secret:
        print "Too low!"
    elif guess>secret:
        print "Too high!"
    tries+=1
if guess==secret:
     print "You got it! Found my secret."
     print "The secret number was", secret
else:
     print "No more guesses! Better luck next time!"
     print "The secret number was",secret
     """
