### T.T.T.#6: nth user

A product to do market research, n users to participate in the activities. 

They give each user a number. 

The first user number is 1, second users numbered 2, and so on...

But no digits 4 and 9 in user's numbers, that is to say the number of 3rd users is 3, the number of 4th users is 5...the number of 8th users is 10... like this:
```
user   1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th ........ nth
number  1   2   3   5   6   7   8  10   11  12  ........ ??
```
Please calculate, how much is the number of the nth user?

#### Rules

Write a function userNumber, argument n means the nth user.

return a user's number by string format.

#### Examples
```
userNumber(1) should return "1"
userNumber(4) should return "5"
userNumber(8) should return "10"
userNumber(10) should return "12"
userNumber(20) should return "25"

