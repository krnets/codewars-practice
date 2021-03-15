### String subpattern recognition I

In this kata you need to build a function to return either true or false if a string can be seen as the repetition of a simpler/shorter subpattern or not.

For example:
```c
HasSubpattern("a") == false; //no repeated pattern
HasSubpattern("aaaa") == true; //created repeating "a"
HasSubpattern("abcd") == false; //no repeated pattern
HasSubpattern("abababab") == true; //created repeating "ab"
HasSubpattern("ababababa") == false; //cannot be entirely reproduced repeating a pattern
```
Strings will never be empty and can be composed of any character (just consider upper- and lowercase letters as different entities) and can be pretty long (keep an eye on performances!).
