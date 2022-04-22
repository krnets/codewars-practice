### Alphabetical Addition

Your task is to add up letters to one letter.

The function will be given an array of letters (chars), each one being a letter to add. Return a char.

Notes:

    Letters will always be lowercase.
    Letters can overflow (see second to last example)
    If no letters are given, 
    the function should return 'z'

Examples:
```c
AddLetters(new char[] {'a', 'b', 'c'}) = 'f'
AddLetters(new char[] {'a', 'b'}) = 'c'
AddLetters(new char[] {'z'}) = 'z'
AddLetters(new char[] {'z', 'a'}) = 'a'
AddLetters(new char[] {'y', 'c', 'b'}) = 'd' // notice the letters overflowing
AddLetters(new char[] {}) = 'z'
