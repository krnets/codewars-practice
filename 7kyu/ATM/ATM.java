/*
There is enough money available on ATM in nominal value
10, 20, 50, 100, 200 and 500 dollars.

You are given money in nominal value of n with 1<=n<=1500.

Try to find minimal number of notes that must be used to repay in dollars,
or output -1 if it is impossible.
*/

/*
public class ATM {
    public int solve(int n) {
        int count = 0;
        var notes = new int[]{500, 200, 100, 50, 20, 10};
        for (int note : notes) {
            while (n >= note) {
                n -= note;
                count++;
            }
        }
        return n == 0 ? count : -1;
    }
}
*/
public class ATM {
    public int solve(int n) {
        int noteCount = 0;
        var denominations = new int[]{500, 200, 100, 50, 20, 10};
        for (int d : denominations) {
            noteCount += n / d;
            n %= d;
        }
        return n > 0 ? -1 : noteCount;
    }
}
