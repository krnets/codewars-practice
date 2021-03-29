### Extension GroupWhile consecutive by the condition items

The method takes in one argument, pred, of the type Func<object, bool> which checks each element of a collection on the satisfaction of a certain condition. The by the order consecutive elements should be grouped while this condition is true (s. example and example tests).

#### Example
```
pred: IsLetter
coll: [ 'L', 'e', 't', 't', 'e', 'r', '1', '2', '4', '=', 'a', 'B', 'E', 'l', 'T', '%' ]

result: [ [ 'L', 'e', 't', 't', 'e', 'r' ], [ '1' ], [ '2' ], [ '4' ], [ '=' ], [ 'a', 'B', 'E', 'l', 'T' ], [ '%' ] ];
