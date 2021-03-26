### Greatest Position Distance Between Matching Array Values

The goal of this Kata is to return the greatest distance of index positions between matching number values in an array or 0 if there are no matching values.

Example: 

In an array with the values [0, 2, 1, 2, 4, 1] the greatest index distance is between the matching '1' values at index 2 and 5. 

Executing greatestDistance against this array would return 3. (i.e. 5 - 2)

Here's the previous example in test form:
```csharp
Assert.AreEqual(3, GreatestDistance.Exec(new List<int> { 0, 2, 1, 2, 4, 1 }));
