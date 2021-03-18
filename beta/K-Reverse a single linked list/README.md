### K-Reverse a single linked list

Given an integer k and a single linked LinkedListNode n of the form:

```csharp
public class LinkedListNode<T>
{
  public T Value { get; set; }
  public LinkedListNode<T> Next { get; set; }
  
  public LinkedListNode() {  }
  
  public LinkedListNode(T value) : this(value, null) {  }
  
  public LinkedListNode(T value, LinkedListNode<T> next)
  {
    Value = value;
    Next = next;
  }
}
```
Split the LinkedList into segments each of length k and reverse them.

The length l of the linked list is guaranteed to be of the form that l % k == 0
Function

Your task is to complete the function
```csharp
public static LinkedListNode<T> KReverse<T>(LinkListNode<T> n, int k)
```
Input: An integer k and the start nodenof the linked list

Output: The 'new' start node of the linked list

Examples
```
Given: k = 2, n = new LinkedListNode<int>(1)

n.Next = new LinkedListNode<int>(2)
n.Next.Next = new LinkedListNode<int>(3)
n.Next.Next.Next = new LinkedListNode<int>(4)

which represents the following linked list L:
[1 => 2 => 3 => 4]

return the following linked list L:
[2 => 1 => 4 => 3]

Given: k = 3
L = [1 => 2 => 3 => 4 => 5 => 6]
return: [3 => 2 => 1 => 6 => 5 => 4]
```
Hint:  It can be done in linear time using constant space
