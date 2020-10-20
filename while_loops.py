# 1a) Uncomment the code below and run it to observe what an infinite loop looks like:
'''
x = 0
while x < 10:
  print(x)
'''

# 1b) Change the boolean expression so instead of it being an infinite loop, it never runs (your change should not result in an error):





# 1c) We can manipulate our variable, such that our boolean expression starts out as true, and then ends up as False. To do this, we can change the value of our
#variable each time through the loop. For example, if we have variable x = 0, and our while loop states while x<10, then we can increase x each time through the loop
#until it is NO LONGER less than 10. Add the line x = x+1 to the while loop above. How many times does the loop run? Describe what the line x = x+1 is doing.







# 2a) There is an even simpler way to write x = x+1 by using an addition assignment operator. Instead of x = x+1, you can say x += 1. Uncomment the while loop below
# and add an x+=2 statement inside of the while loop, but after the print function. How many times does the loop run? Describe what x+=2 is doing.
'''
x = 0
while x < 10:
  print(x)
'''


# 2b) Similar to the += operator, there are subtraction assignment (-=), multiplication assignment (*=) and division assignment (/=) operators. Uncomment the code
#below and write a boolean expression for your while loop so it doesn't get stuck in an infinite loop:

'''
x = 100
while (#add a boolean expression here):
  print(x)
  x/=1.00001
'''



# 2c) Write a while loop that prints all even numbers in descending order from 100 to 0, and have it stop when it reaches 0. HINT: Use the -= operator.








# 3) While loops are also similar to if statements because they can have an alternative else statement! Write a while loop that prints the integers 1-50 
#using variable num, and after the loop is done, include an else statement that prints "num is no longer less than 50."










# 4) You can also have conditional statements inside your while loop. Write a while loop that iterates from 1-10. When your variable equals 3, print 'Your variable
#is equal to 3!', when your variable equals 6, print '6 is double 3!', when your variable equals 9 print '9 is triple 3!', and for every other number print 'Not 3,
#6 or 9.' HINT: Your boolean expression for your while loop should look like variable_name <= 10, and you should increment with variable_name += 1.

















##--------------------------------------------BONUS QUESTIONS------------------------------------------------##

# 1) Using a while loop, create a program that tells the user that every number from 0-100 is either an odd number or an even number. For example, it should print
# '1 is an odd number!', '2 is an even number', '3 is an odd number', etc. HINT: You will need conditionals inside of your while loop, and you will probably need to
#use the modulo operator.








# 2) Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. HINT: You need to use a continue statement.








# 3) Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five 
#print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". HINT: Modulo operator is your friend.







# 4) Create a guessing game using random.randint(). Create a random integer variable, and an input variable where the user can guess a number. Then use a while loop
#that checks the user's guess to see if it matches up with the random number generated, and then provides feedback to help the user make a better guess.
#For example, if your guess is greater than the random number, tell the user "too high, try again!" Provide similar feedback if the guess is too low. Then exit the while
#loop once the user guesses correctly, and tell the user they've won. This is the same bonus as the last assignment, but can you do it again? Practice makes perfect!








