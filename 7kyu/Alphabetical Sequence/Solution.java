/*
In this kata you will be given a random string of letters and tasked
with returning them as a string of comma-separated sequences sorted alphabetically,
with each sequence starting with an uppercase character followed by n-1 lowercase characters,
where n is the letter's alphabet position 1-26.


        alphaSeq("ZpglnRxqenU") ->
        "Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Xxxxxxxxxxxxxxxxxxxxxxxx,Zzzzzzzzzzzzzzzzzzzzzzzzzz"

        The string will include only letters.
        The first letter of each sequence is uppercase followed by n-1 lowercase.
        Each sequence is separated with a comma.
        Return value needs to be a string.
*/


import java.util.stream.Collectors;

/*
public class Solution {
    public static String alphaSeq(String s) {
        return s.toUpperCase().chars()
                .sorted()
                .mapToObj(c -> ((char) c + "").toUpperCase() + ((char) c + "").repeat(c - 'A').toLowerCase())
                .collect(Collectors.joining(","));
    }
}
*/
/*
public class Solution {
    public static String alphaSeq(String s) {
        return s.toLowerCase().chars()
                .sorted()
                .mapToObj(c -> ((char) c + "").toUpperCase() + ((char) c + "").repeat(c - 'a'))
                .collect(Collectors.joining(","));
    }
}
*/
public class Solution {
    public static String alphaSeq(String s) {
        return s.toUpperCase().chars()
                .sorted()
                .mapToObj(c -> (char) c + ((char) c + "").repeat(c - 'A').toLowerCase())
                .collect(Collectors.joining(","));
    }
}
