class Dinglemouse
{
    private static string ALPHABET = Preloaded.ALPHABET;

    public static string[] FlapDisplay(string[] lines, int[][] rotors)
    {
        for (int row = 0; row < lines.Length; row++)
        {
            var array = lines[row].ToCharArray();

            for (int col = 0; col < rotors[row].Length; col++)
            {
                array[col] = (char) (array[col] + rotors[row][i]);
            }

            lines[row] = string.Concat(array);
        }

        return lines;
    }
}

// chars[i] = (char) (chars[i] + rotors[i][j]);
// private static string ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789";