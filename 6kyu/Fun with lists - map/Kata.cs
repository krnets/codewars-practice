using System;

class Kata
{
    public static Node<R> Map<T, R>(Node<T> head, Func<T, R> f)
    {
        if (head == null)
            return null;

        var current = new Node<R>(f(head.data));
        var newHead = current;

        while (head.next != null)
        {
            head = head.next;
            current.next = new Node<R>(f(head.data));
            current = current.next;
        }

        return newHead;
    }
}


/*using System;

class Kata
{
    public static Node<R> Map<T, R>(Node<T> head, Func<T, R> f)
    {
        return head == null ? null : new Node<R>(f(head.data), Map(head.next, f));
    }
}*/