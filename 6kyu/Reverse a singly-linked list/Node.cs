using System;
using System.Collections.Generic;
using System.Linq;

public class Node : object
{
    public int Value;
    public Node Next;
  
    // Classic constructor
    public Node(int value, Node next = null)
    {
        this.Value = value;
        this.Next = next;
    }
  
    // Constructor for IEnumerable<int>s
    // Makes it easier to construct large lists
    public Node(IEnumerable<int> values)
    {
        if (values == null || !values.Any()) { throw new ArgumentException("Node(IEnumerable<int>)'s first argument must not be empty."); }
        Node node = null;
    
        foreach(int value in Enumerable.Reverse(values))
        {
            node = new Node(value, node);
        }
    
        this.Value = node.Value;
        this.Next = node.Next;
    }

    // Override which allows user to "print" node and view data values
    // Example:
    // new Node(3, new Node(2, new Node(1, null))) -> "3 -> 2 -> 1 -> null"
    public override string ToString()
    {
        List<int> result = new List<int>();
        Node curr = this;
    
        while (curr != null)
        {
            result.Add(curr.Value);
            curr = curr.Next;
        }
    
        return String.Join(" -> ", result) + " -> null";
    }
  
    public override bool Equals(Object obj)
    {
        // Check for null values and compare run-time types.
        if (obj == null || GetType() != obj.GetType()) { return false; }
  
        return this.ToString() == obj.ToString();
    }
}