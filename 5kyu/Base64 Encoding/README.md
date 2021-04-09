### Base64 Encoding

Create a function that converts the value of the string to/from Base64 using the ASCII (UTF-8 for C#) character set.

Do not use built in functions.

Usage:
```c
// should return 'dGhpcyBpcyBhIHN0cmluZyEh'
Base64Utils.ToBase64("this is a string!!");

// should return 'this is a string!!'
Base64Utils.FromBase64("dGhpcyBpcyBhIHN0cmluZyEh");
````
You can learn more about Base64 encoding and decoding [here](http://en.wikipedia.org/wiki/Base64).

Note: This kata uses the non-padding version ("=" is not added to the end).

