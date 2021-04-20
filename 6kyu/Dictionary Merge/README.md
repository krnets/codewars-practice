### Dictionary Merge

Your task is to implement a function that takes one or more dictionaries and combines them in one result dictionary.

The keys in the given dictionaries can overlap. In that case you should combine all source values in an array. Duplicate values should be preserved.

Here is an example:
```c
var source1 = new Dictionary<string, int>{{"A", 1}, {"B", 2}}; 
var source2 = new Dictionary<string, int>{{"A", 3}};
```
Dictionary<string, int[]> result = DictionaryMerger.Merge(source1, source2);
// result should have this content: {{"A", [1, 3]}, {"B", [2]}}

You can assume that only valid dictionaries are passed to your function. 

The number of given dictionaries might be large. So take care about performance.

