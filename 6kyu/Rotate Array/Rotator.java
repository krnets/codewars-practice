/*
Create a method named "rotate" that returns a given array
with the elements inside the array rotated n spaces.

If n is greater than 0 it should rotate the array to the right.
If n is less than 0 it should rotate the array to the left.
If n is 0, then it should return the array unchanged.

Example:

        Object[] data = new Object[]{1, 2, 3, 4, 5};

        rotate(data, 1)    =>    {5, 1, 2, 3, 4}
        rotate(data, 2)    =>    {4, 5, 1, 2, 3}
        rotate(data, 3)    =>    {3, 4, 5, 1, 2}
        rotate(data, 4)    =>    {2, 3, 4, 5, 1}
        rotate(data, 5)    =>    {1, 2, 3, 4, 5}

        rotate(data, 0)    =>    {1, 2, 3, 4, 5}

        rotate(data, -1)    =>    {2, 3, 4, 5, 1}
        rotate(data, -2)    =>    {3, 4, 5, 1, 2}
        rotate(data, -3)    =>    {4, 5, 1, 2, 3}
        rotate(data, -4)    =>    {5, 1, 2, 3, 4}
        rotate(data, -5)    =>    {1, 2, 3, 4, 5}

Furthermore the method should take ANY array of objects and perform this operation on them:

        rotate(new Object[]{'a', 'b', 'c'}, 1)        =>    {'c', 'a', 'b'}
        rotate(new Object[]{1.0, 2.0, 3.0}, 1)        =>    {3.0, 1.0, 2.0}
        rotate(new Object[]{true, true, false}, 1)    =>    {false, true, true}

Finally the rotation shouldn't be limited by the indices available in the array.
Meaning that if we exceed the indices of the array it keeps rotating.

Example:

        Object[] data = new Object[]{1, 2, 3, 4, 5}

        rotate(data, 7)        =>    {4, 5, 1, 2, 3}
        rotate(data, 11)       =>    {5, 1, 2, 3, 4}
        rotate(data, 12478)    =>    {3, 4, 5, 1, 2}
*/

/*
public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        var arr = new Object[data.length];
        int len = n % data.length + (n < 0 ? data.length : 0);

        if (data.length - len >= 0) {
            System.arraycopy(data, 0, arr, len, data.length - len);
        }
        System.arraycopy(data, data.length - len, arr, 0, len);

        return arr;
    }
}
*/

/*
public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        int len = data.length;
        var arr = new Object[len];

        int rotateBy = ((n % len) + len) % len;
        int offset = len - rotateBy;

        System.arraycopy(data, 0, arr, rotateBy, offset);
        System.arraycopy(data, offset, arr, 0, rotateBy);

        return arr;
    }
}
*/

/*
public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        var arr = new Object[data.length];
        int len = n % data.length + (n < 0 ? data.length : 0);

        for (int i = len; i < data.length; i++) {
            arr[i] = data[i - len];
        }
        for (int i = 0; i < len; i++) {
            arr[i] = data[data.length - len + i];
        }

        return arr;
    }
}
*/

/*
public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        var arr = new Object[data.length];
        int len = n % data.length + (n < 0 ? data.length : 0);

        for (int i = 0; i < data.length; i++) {
            if (i < len)
                arr[i] = data[data.length - len + i];
            else
                arr[i] = data[i - len];
        }
        return arr;
    }
}
*/

/*public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        var arr = new Object[data.length];
        int len = n % data.length + (n < 0 ? data.length : 0);

        for (int i = 0; i < data.length; i++) {
            if (i < len)
                arr[i] = data[data.length - len + i];
            else
                arr[i] = data[i - len];
        }
        return arr;
    }
}*/

/*
public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        int len = data.length;
        var arr = new Object[len];

        for (int i = 0; i < len; i++) {
            arr[i] = data[((i - n) % len + len) % len];
        }
        return arr;
    }
}
*/

/*
public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        var arr = new Object[data.length];

        for (int i = 0; i < data.length; i++) {
            arr[i] = data[Math.floorMod(i - n, data.length)];
        }
        return arr;
    }
}
*/


/*
import java.util.stream.IntStream;

public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        return IntStream.range(0, data.length)
                .mapToObj(i -> data[Math.floorMod(i - n, data.length)])
                .toArray();
    }
}
*/

import java.util.Arrays;
import java.util.Collections;

public class Rotator {
    public Object[] rotate(Object[] data, int n) {
        Collections.rotate(Arrays.asList(data), n);
        return data;
    }
}
