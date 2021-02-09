### Linked Lists - Length & Count

Implement Length() to count the number of nodes in a linked list.
```
Node.Length(nullptr) => 0
Node.Length(1 -> 2 -> 3 -> nullptr) => 3
```
Implement Count() to count the occurrences of a that satisfy a condition provided by a predicate which takes in a node's Data value.
```
Node.Count(null, value => value == 1) => 0
Node.Count(1 -> 3 -> 5 -> 6, value => value % 2 != 0) => 3
```
I've decided to bundle these two functions within the same Kata since they are both very similar.

The push()/Push() and buildOneTwoThree()/BuildOneTwoThree() functions do not need to be redefined.
