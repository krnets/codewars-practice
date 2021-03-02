/*
public static class Kata
{
    public static int SumTree(Node root)
    {
        if (root == null) return 0;

        int sum = root.Value;

        sum += SumTree(root.Left);
        sum += SumTree(root.Right);

        return sum;
    }
}
*/

public static class Kata
{
    public static int SumTree(Node root)
    {
        return root == null ? 0 : root.Value + SumTree(root.Left) + SumTree(root.Right);
    }
}

public class Node
{
    public int Value;
    public Node Left;
    public Node Right;

    public Node(int value, Node left = null, Node right = null)
    {
        Value = value;
        Left = left;
        Right = right;
    }
}