### Guess the number!

The `Guesser` class is set up to generate a random number from 1-1000, and allows 10 guesses to get the number.

Your task is to write a method `getNumber()` inside the `Guesser` class to identify a random number from 1-1000.

You should use the method:
```java
guess(number)
```
Which will return either:
```
"Too high!" If the guess is too high.
"Too low!" If the guess is too low.
or "Correct!" If the guess is correct.
```

You can only call this method 10 times before an exception is raised.
