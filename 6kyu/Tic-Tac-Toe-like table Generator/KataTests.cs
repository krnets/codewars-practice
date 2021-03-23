using NUnit.Framework;

public class SampleTest
{
    [Test]
    public void BasicTest1()
    {
        DoTest(new char[] {'O', 'X', 'X', 'O'}, 2, " O | X \n-------\n X | O "); // 7 = 8 - 1
    }

    [Test]
    public void BasicTest2()
    {
        DoTest(new char[] {'O', 'X', ' ', ' ', 'X', ' ', 'X', 'O', ' '}, 3, // 11 = 12 - 1
            " O | X |   \n-----------\n   | X |   \n-----------\n X | O |   ");
    }

    [Test]
    public void BasicTest3()
    {
        DoTest(new char[] {'O', 'X', ' ', ' ', 'X', ' ', 'X', 'O', ' ', 'O'}, 5, // 19 = 20 - 1
            " O | X |   |   | X \n-------------------\n   | X | O |   | O ");
    }

    [Test]
    public void BasicTest4()
    {
        DoTest(new char[] {'O', 'X', ' ', ' ', 'X', ' ', 'X', 'O', ' ', 'O'}, 2,
            " O | X \n-------\n   |   \n-------\n X |   \n-------\n X | O \n-------\n   | O ");
    }

    [Test]
    public void BasicTest5()
    {
        DoTest(
            new char[]
            {
                '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1',
                '2', '3', '4', '5', '1', '2', '3', '4', '5', '1', '2', '3', '4', '5', '1'
            }, 6,
            " 1 | 2 | 3 | 4 | 5 | 1 \n-----------------------\n 2 | 3 | 4 | 5 | 1 | 2 \n-----------------------\n 3 | 4 | 5 | 1 | 2 | 3 \n-----------------------\n 4 | 5 | 1 | 2 | 3 | 4 \n-----------------------\n 5 | 1 | 2 | 3 | 4 | 5 \n-----------------------\n 1 | 2 | 3 | 4 | 5 | 1 ");
    }

    private void DoTest(char[] board, int width, string expected)
    {
        Assert.AreEqual(expected, Kata.DisplayBoard(board, width));
    }
}