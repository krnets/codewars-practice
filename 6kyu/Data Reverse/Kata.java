/*
A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

        11111111  00000000  00001111  10101010
        (byte1)   (byte2)   (byte3)   (byte4)

        should become:

        10101010  00001111  00000000  11111111
        (byte4)   (byte3)   (byte2)   (byte1)

The total number of bits will always be a multiple of 8.

        The data is given in an array as such:

        [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
*/

/*
public class Kata {
    public static int[] DataReverse(int[] data) {
        int[] result = new int[data.length];

        for (int i = 0; i < data.length; i += Byte.SIZE)

            for (int j = 0, k = data.length - Byte.SIZE - i; j < Byte.SIZE; j++)

                result[k + j] = data[i + j];

        return result;
    }
}*/

/*
public class Kata {
    public static int[] DataReverse(int[] data) {
        int[] reversedData = new int[data.length];

        for (int i = 0; i < data.length; i++)
            reversedData[i] = data[data.length + (i % Byte.SIZE) - Byte.SIZE * (i / Byte.SIZE + 1)];

        return reversedData;
    }
}
*/

public class Kata {
    public static int[] DataReverse(int[] data) {
        int[] reversedData = new int[data.length];
        int i = data.length - Byte.SIZE;
        int j = 0;

        while (i >= 0) {
            System.arraycopy(data, i, reversedData, j, Byte.SIZE);
            i -= Byte.SIZE;
            j += Byte.SIZE;
        }
        return reversedData;
    }
}

