using System.Collections.Generic;

static class Harmonizer
{
    public static string Transpose(string noteName, int transposition)
    {
        var notes = new List<string> {"C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"};

        return notes[(notes.IndexOf(noteName) + transposition + notes.Count) % notes.Count];
    }
}