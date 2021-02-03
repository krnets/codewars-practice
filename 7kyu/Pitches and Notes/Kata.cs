/*using System.Collections.Generic;

public static partial class Kata
{
    public static Dictionary<double, string> NotesDictionary = new()
    {
        {440, "A"},
        {466.16, "A#"},
        {493.88, "B"},
        {523.25, "C"},
        {554.37, "C#"},
        {587.33, "D"},
        {622.25, "D#"},
        {659.25, "E"},
        {698.46, "F"},
        {739.99, "F#"},
        {783.99, "G"},
        {830.61, "G#"}
    };

    public static string GetNote(double pitch)
    {
        foreach (var pair in NotesDictionary)
            if (pair.Key % pitch == 0 || pitch % pair.Key == 0)
                return pair.Value;

        return string.Empty;
    }
}*/

using System.Collections.Generic;
using System.Linq;

public static partial class Kata
{
    public static Dictionary<double, string> NotesDictionary = new()
    {
        {440, "A"},
        {466.16, "A#"},
        {493.88, "B"},
        {523.25, "C"},
        {554.37, "C#"},
        {587.33, "D"},
        {622.25, "D#"},
        {659.25, "E"},
        {698.46, "F"},
        {739.99, "F#"},
        {783.99, "G"},
        {830.61, "G#"}
    };

    public static string GetNote(double pitch)
    {
        return NotesDictionary.Single(p => p.Key % pitch == 0 || pitch % p.Key == 0).Value;
    }
}