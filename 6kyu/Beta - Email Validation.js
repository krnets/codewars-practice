// Beta - Email Validation

/* Write a function to test whether a given input is a valid email address.

For the purposes of this kata, here is what makes a valid email:

    At least one letter character at the beginning
    All characters between the first character and the @ (if any) must be letters, numbers, or underscores
    There must be an @ character (after the points listed just now)
    After the @ character, there must be at least one word character (letter, number, or underscore) or hyphen
    The email must end with at least one set of a dot followed by one or more word characters.
    The input must NOT be case-sensitive

The function should return true or false.
Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings | Validation | Algorithms */

const validate = (input) => /^[a-z]\w*@[a-z\-\_0-9]+(\.\w{1,})+$/.test(input)

q = validate('abc@example.com') // true, "'abc@example.com' should return true"
q
q = validate('_bc@example.com') // false, "'_bc@example.com' should return false"
q
q = validate('abc_123@a-1_23.co.uk') // true, "'abc_123@a-1_23.co.uk' should return true"
q
q = validate('abc@abc') // false, "'abc@abc' should return false"
q
q = validate('abc@example.com#') // false
q
q = validate('b@l.com') // true
q
q = validate('iy_5-vrwpdsk5@2gjr7dxtro.de') // false
q