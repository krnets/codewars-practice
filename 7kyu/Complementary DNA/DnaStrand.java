/*
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions"
for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
You have function with one side of the DNA string; you need to get the other complementary side.
DNA strand is never empty or there is no DNA at all.

More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

DnaStrand.makeComplement("ATTGC") // return "TAACG"
DnaStrand.makeComplement("GTAT") // return "CATA"
*/

import java.util.Map;

public class DnaStrand {
    public static String makeComplement(String dna) {
        var trans = Map.of('A', 'T', 'T', 'A', 'C', 'G', 'G', 'C');
        var result = new StringBuilder();
        for (char c : dna.toCharArray())
            result.append(trans.get(c));
        return result.toString();
    }
}