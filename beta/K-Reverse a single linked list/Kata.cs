public class Kata
{
    public static LinkedListNode<T> KReverse<T>(LinkedListNode<T> node, int k)
    {
        LinkedListNode<T> prevNode = null, currNode = node, nextNode = null;
        int count = 0;

        while (count < k && currNode != null)
        {
            nextNode = currNode.Next;
            currNode.Next = prevNode;

            prevNode = currNode;
            currNode = nextNode;

            count++;
        }

        if (currNode != null)
            node.Next = KReverse<T>(currNode, k);

        return prevNode;
    }
}