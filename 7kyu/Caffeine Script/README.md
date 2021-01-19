### Caffeine Script

Complete the function caffeineBuzz, which takes a non-zero integer as it's one argument.

If the integer is divisible by 3, return the string "Java".

If the integer is divisible by 3 and divisible by 4, return the string "Coffee"

If the integer is one of the above and is even, add "Script" to the end of the string.

Otherwise, return the string "mocha_missing!"
```c
Kata.CaffeineBuzz(1)   => "mocha_missing!"
Kata.CaffeineBuzz(3)   => "Java"
Kata.CaffeineBuzz(6)   => "JavaScript"
Kata.CaffeineBuzz(12)  => "CoffeeScript"
