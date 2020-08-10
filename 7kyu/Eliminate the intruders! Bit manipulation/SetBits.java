/*
You are given a string representing a number in binary.
Your task is to delete all the unset bits in this string and
return the corresponding number (after keeping only the '1's).

In practice, you should implement this function:

    public long eliminateUnsetBits(String number);

Examples

        eliminateUnsetBits("11010101010101") ->  255 (= 11111111)
        eliminateUnsetBits("111") ->  7
        eliminateUnsetBits("1000000") -> 1
        eliminateUnsetBits("000") -> 0
*/

/*
public class SetBits {
    public long eliminateUnsetBits(String number) {
        return number == null || number.equals("") ? 0 : Long.parseLong(number.replaceAll("0", ""), 2);
    }
}*/

public class SetBits {
    public long eliminateUnsetBits(String number) {
        var x = number.replace("0", "");
        return x.isEmpty() ? 0 : Long.parseLong(x, 2);
    }
}

/*
public class SetBits {
    public long eliminateUnsetBits(String number) {
        return (1L << number.replace("0", "").length()) - 1;
    }
}
*/

/*
public class SetBits {
    public long eliminateUnsetBits(String number) {
        return (long) Math.pow(2, number.replace("0", "").length()) - 1;
    }
}
*/
