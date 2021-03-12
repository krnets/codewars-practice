using System;

public class Node<T> : IEquatable<Node<T>>
{
    public T data;
    public Node<T> next;

    public Node(T data)
    {
        this.data = data;
    }

    public Node(T data, Node<T> next)
    {
        this.data = data;
        this.next = next;
    }

    public bool Equals(Node<T> other)
    {
        return other.data.Equals(data);
    }
}