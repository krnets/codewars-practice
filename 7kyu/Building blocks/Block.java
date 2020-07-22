/*
Write a class Block that creates a block

        ##Requirements
        The constructor should take an array as an argument, this will contain 3 integers of the form
        [width, length, height] from which the Block should be created.

        Define these methods:

        `getWidth()` return the width of the `Block`
        `getLength()` return the length of the `Block`
        `getHeight()` return the height of the `Block`
        `getVolume()` return the volume of the `Block`
        `getSurfaceArea()` return the surface area of the `Block`

        ##Examples

        Block b = new Block(new int[]{2,4,6}) -> creates a `Block` object with a width of `2` a length of `4` and a height of `6`
        b.getWidth() // -> 2
        b.getLength() // -> 4
        b.getHeight() // -> 6
        b.getVolume() // -> 48
        b.getSurfaceArea() // -> 88

        Note: no error checking is needed
*/

/*
public class Block {
    private final int width;
    private final int length;
    private final int height;

    public Block(int[] dimensions) {
        this.width = dimensions[0];
        this.length = dimensions[1];
        this.height = dimensions[2];
    }

    public int getWidth() {
        return this.width;
    }

    public int getLength() {
        return this.length;
    }

    public int getHeight() {
        return this.height;
    }

    public int getVolume() {
        return this.width * this.length * this.height;
    }

    public int getSurfaceArea() {
        return (2 * this.length * this.width) + (2 * this.width * this.height) + (2 * this.height * this.length);
    }
}*/

import java.util.stream.IntStream;

public class Block {
    private final int width;
    private final int length;
    private final int height;

    public Block(int[] dimensions) {
        if (dimensions != null && IntStream.of(dimensions).allMatch(v -> v > 0)) {
            width = dimensions[0];
            length = dimensions[1];
            height = dimensions[2];
        } else {
            throw new IllegalArgumentException("3 positive values required");
        }
    }

    public int getWidth() {
        return width;
    }

    public int getLength() {
        return length;
    }

    public int getHeight() {
        return height;
    }

    public int getVolume() {
        return width * length * height;
    }

    public int getSurfaceArea() {
        return 2 * (length * width + width * height + height * length);
    }
}
