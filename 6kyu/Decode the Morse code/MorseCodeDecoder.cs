using System.Collections.Generic;

class MorseCodeDecoder
{
    public static string Decode(string morseCode)
    {
        var wordsInMorse = morseCode.Trim().Split("  ");
        var wordsDecoded = new List<string>();

        foreach (var word in wordsInMorse)
        {
            var charsInMorse = word.Split();
            var charsDecoded = new List<string>();

            foreach (var s in charsInMorse)
                charsDecoded.Add(MorseCode.Get(s));

            wordsDecoded.Add(string.Concat(charsDecoded));
        }

        return string.Join(" ", wordsDecoded);
    }
}