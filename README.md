# While Loops

A while loop is structured very similarly to a conditional if statement. For example, an if statement says the word IF, it has a **boolean expression** (e.g. x>=10), a colon, and then some code indented inside of it. Like below:
```
x=5
if x == 5:
  print(x)
```

A while loop takes on the exact same structure, except you replace the word **if** with **while**. Observe:
```
y=5
while y == 5:
  print(y)
```

There is one major fundamental difference between how these two blocks of code run, however. An if statement can either run **one time** or **zero times**. Those are the only two options for an if statement. With a while loop, it can run **0,1,2,3...∞** number of times. **A while loop will run continuously until an exit condition is met**. This means that it will run until the boolean expression is no longer true.

This means that you have to have a way to change your variable so that your boolean expression eventually evaluates to False. If your boolean expression is always True, then you can get stuck inside an INFINITE LOOP. In fact, the block of code above this paragraph will get you stuck inside an infinite loop. If your Boolean expression is always False, then the code inside your while loop will NEVER run. We need to figure out a way to start our Boolean expression as True, and then make it False at some point further on.

Navigate to the .py file to learn more about while loops!
