public class Kata
{
    public bool ChessBoardCellColor(string cell1, string cell2)
    {
        var board = new int[8, 8];

        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                if ((i % 2 == 0 && j % 2 == 0) || (i % 2 == 1 && j % 2 == 1))
                    board[i, j] = 1;
            }
        }

        return board[cell1[0] - 'A', cell1[1] - '0' - 1] ==
               board[cell2[0] - 'A', cell2[1] - '0' - 1];
    }
}

/*public class Kata
{
    public bool ChessBoardCellColor(string cell1, string cell2)
    {
        return (cell1[0] + cell2[0] + cell1[1] + cell2[1]) % 2 == 0;
    }
}*/