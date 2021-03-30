### Delta Generators

In mathematics, the symbols Δ and d are often used to denote the difference between two values. 

Similarly, differentiation takes the ratio of changes (ie. dy/dx) for a linear relationship. 

This method can be applied multiple times to create multiple 'levels' of rates of change. 

(A common example is x (position) -> v (velocity) -> a (acceleration)).

Today we will be creating a similar concept. 

Our function delta will take a list values and a positive integer level, and return a list with the 'differences' of the original values. 

(Differences here means strictly b - a, eg. [1, 3, 2] => [2, -1]) 

The argument level is the 'level' of difference, for example acceleration is the 2nd 'level' of difference from position. 

The specific encoding of input and output lists is specified below.

The example below shows three different 'levels' of the same input.
```csharp
int[] input = new [] {1, 2, 4, 7, 11, 16, 22};
Delta(input, 1);  // new [] {1, 2, 3, 4, 5, 6}
Delta(input, 2);  // new [] {1, 1, 1, 1, 1}
Delta(input, 3);  // new [] {0, 0, 0, 0}
```
We do not assume any 'starting value' for the list, and so each subsequent list will be one item shorter than the previous (as shown above).

If an infinite list is provided as input, then the output must also be infinite.

#### Input/Output list encoding

Input and output lists can be any, possibly infinite, IEnumerable<int>. 

Possibilities include finite lists and possibly infinite generator objects, but any Enumerable<int> must be accepted as input and is acceptable as output.

Difference implementation

* Delta must work for lists of any int instance.

Additional Requirements/Notes:

* delta must work for inputs which are infinite
* values will always be valid, and will always produce consistent classes/types of object
* level will always be valid, and 1 <= level <= 400

Additional examples:

```csharp
IEnumerable<int> Up() {
  int a=0, b=1; while (true) { yield return a; (a, b) = (a + b, b + 3); } 
}
Delta(Up(), 1).Take(10);  // new[] {1,4,7,10,13,16,19,22,25,28}
