### Remember

Write a function that takes a string and returns an array of the repeated characters (letters, numbers, whitespace) in the string.

If a charater is repeated more than once, only show it once in the result array.

Characters should be shown by the order of their first repetition. Note that this may be different from the order of first appearance of the character.

Characters are case sensitive.

Examples:
```python
Remember("apple") => returns ['p']
Remember("apPle") => returns []          # no repeats, 'p' != 'P'
Remember("pippi") => returns ['p','i']   # show 'p' only once
Remember('Pippi') => returns ['p','i']   # 'p' is repeated first
