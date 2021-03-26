using System.Linq;

public class Kata
{
    public bool PairOfShoes(int[][] shoes)
    {
        return shoes.GroupBy(shoeSize => shoeSize[1])
            .All(g => g.Count(pair => pair[0] == 0) == g.Count(pair => pair[0] == 1));
    }
}