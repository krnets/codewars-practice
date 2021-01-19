### Ordered Count of Characters

Count the number of occurrences of each character and return it as a list of tuples in order of appearance. For empty output return an empty list.

Example:
```c
Kata.OrderedCount("abracadabra") == new List<Tuple<char, int>> () {
  new Tuple<char, int>('a', 5),
  new Tuple<char, int>('b', 2),
  new Tuple<char, int>('r', 2), 
  new Tuple<char, int>('c', 1),
  new Tuple<char, int>('d', 1)
}
