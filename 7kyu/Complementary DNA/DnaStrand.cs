/*using System.Text;

public class DnaStrand
{
    public static string MakeComplement(string dna)
    {
        var sb = new StringBuilder();

        foreach (char c in dna)
            switch (c)
            {
                case 'A': sb.Append('T'); break;
                case 'C': sb.Append('G'); break;
                case 'G': sb.Append('C'); break;
                case 'T': sb.Append('A'); break;
            }

        return sb.ToString();
    }
}*/

using System.Linq;

public class DnaStrand
{
    public static string MakeComplement(string dna)
    {
        return string.Concat(dna.Select(c => "ACGT"["TGCA".IndexOf(c)]));
    }
}