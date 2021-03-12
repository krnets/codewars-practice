### Fun with lists: map

Implement the method map, which accepts a linked list (head) and a mapping function, and returns a new linked list (head) where every element is the result of applying the given mapping method to each element of the original list.

For example: 

Given the list: 1 -> 2 -> 3, and the mapping function x => x * 2, map should return 2 -> 4 -> 6

The linked list is defined as follows:

```csharp
class Node<T> 
{
    public T data;
    public Node<T> next;
    
    public Node<T>(T data){
        this.data = data;
    }
    
    public Node<T>(T data, Node<T> next){
        this.data = data;
        this.next = next;
    }
}
```
Note: the list may be null and can hold any type of value.
