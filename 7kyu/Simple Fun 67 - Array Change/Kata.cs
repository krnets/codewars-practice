namespace myjinxin
{
    public class Kata
    {
        public int ArrayChange(int[] arr)
        {
            int moves = 0;

            for (int i = 1; i < arr.Length; i++)
            {
                while (arr[i - 1] >= arr[i])
                {
                    arr[i]++;
                    moves++;
                }
            }

            return moves;
        }
    }
}