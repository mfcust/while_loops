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
