public class LinkedListNode<T>
{
    public T Value { get; set; }
    public LinkedListNode<T> Next { get; set; }

    public LinkedListNode()
    {
    }

    public LinkedListNode(T value) : this(value, null)
    {
    }

    public LinkedListNode(T value, LinkedListNode<T> next)
    {
        Value = value;
        Next = next;
    }
}