import java.util.Arrays;
import java.util.stream.Collectors;

public class Kata {
    public static long nextSmaller(long n) {
        int[] digits = String.valueOf(n)
                .chars()
                .map(Character::getNumericValue)
                .toArray();

        // iterate through the digits from right to left
        // at each iteration try to find the largest digit to the right
        // that is smaller than current digit
        int startingIndex = digits.length - 1;

        for (int i = digits.length - 2; i >= 0; i--) {
            // don't allow 0 to be a max when comparing to first digit
            // This stops leading zero issues
            int max = i == 0 ? 0 : Integer.MIN_VALUE;
            int maxIndex = -1;

            for (int j = i + 1; j < digits.length; j++) {
                // find and save max that is less than current
                if (digits[j] > max && digits[j] < digits[i]) {
                    max = digits[j];
                    maxIndex = j;
                }
            }

            // if digit found, swap and break out of the loop
            if (maxIndex >= 0) {
                swap(digits, maxIndex, digits[i], i);
                startingIndex = i;
                break;
            }
        }

        // sort the remaining digits descending
        // to get the largest number that is less than n
        for (int i = startingIndex + 1; i < digits.length - 1; i++) {
            int max = digits[i];
            int sortIndex = i;

            for (int j = i; j < digits.length; j++) {
                if (digits[j] > max) {
                    max = digits[j];
                    sortIndex = j;
                }
            }
            swap(digits, i, max, sortIndex);
        }

        // Convert back to a long and return
        String digitsJoined = Arrays.stream(digits)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining());

        long result = Long.parseLong(digitsJoined);

        return result == n ? -1 : result;
    }

    private static void swap(int[] digits, int i, int max, int sortIndex) {
        int temp = digits[i];
        digits[i] = max;
        digits[sortIndex] = temp;
    }
}
