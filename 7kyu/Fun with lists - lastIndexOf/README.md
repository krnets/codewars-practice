### Fun with lists: lastIndexOf

Implement the method lastIndexOf, which accepts a linked list (head) and a value, and returns the index (zero based) of the last occurrence of that value if exists, or -1 otherwise.

For example: Given the list: 1 -> 2 -> 3 -> 3, and the value 3, `lastIndexOf` should return 3.

The linked list is defined as follows:
```kotlin
data class Node(val data: Any?, val next: Node?=null)
```
Note: the list may be null and can hold any type of value.
