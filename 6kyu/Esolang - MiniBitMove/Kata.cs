public class Kata
{
    public static bool[] Interpreter(string tape, bool[] array)
    {
        for (int i = 0, p = 0; p < array.Length; i++)
            if (tape[i % tape.Length] == '1')
                array[p] = !array[p];
            else p++;

        return array;
    }
}