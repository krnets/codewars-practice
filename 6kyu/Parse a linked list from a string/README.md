### Parse a linked list from a string

Preloaded for you is a class, struct or derived data type Node (depending on the language) used to construct linked lists in this Kata:
```c#
public class Node : Object
{
  public int Data;
  public Node Next;

  public Node(int data, Node next = null)
  {
    this.Data = data;
    this.Next = next;
  }

  public override bool Equals(Object obj)
  {
    // Check for null values and compare run-time types.
    if (obj == null || GetType() != obj.GetType()) { return false; }

    return this.ToString() == obj.ToString();
  }

  public override string ToString()
  {
    List<int> result = new List<int>();
    Node curr = this;

    while (curr != null)
    {
      result.Add(curr.Data);
      curr = curr.Next;
    }

    return String.Join(" -> ", result) + " -> null";
  }
}
```
Create a function parse which accepts exactly one argument string which is a string representation of a linked list. 

Your function must return the corresponding linked list, constructed from instances of the Node class. 

The string representation of a list has the following format: 

the value of the node, followed by a whitespace, an arrow and another whitespace (" -> "), 

followed by the rest of the linked list. 

Each string representation of a linked list will end in "null". 

For example, given the following string representation of a linked list:

"1 -> 2 -> 3 -> null"

... your function should return:

new Node(1, new Node(2, new Node(3)))

Note that due to the way the constructor for Node is defined, if a second argument is not provided, the Next field is automatically set to null. 

That means your function could also return the following (if it helps you better visualise what is actually going on):

new Node(1, new Node(2, new Node(3, null)))

Another example: given the following string input:

"0 -> 1 -> 4 -> 9 -> 16 -> null"

... your function should return:

new Node(0, new Node(1, new Node(4, new Node(9, new Node(16)))))

If the input string is just "null", return null.

For the simplicity of this Kata, the values of the nodes in the string representation will always ever be non-negative integers, so the following would not occur: 

"Hello World -> Goodbye World -> 123 -> null"

This also means that the values of each Node must also be non-negative integers so keep that in mind when you are parsing the list from the string.
