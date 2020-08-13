/*
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String,
which must take in input array, containing the names of people who like an item.
It must return the display text as shown in the examples:

        likes {} // must be "no one likes this"
        likes {"Peter"} // must be "Peter likes this"
        likes {"Jacob", "Alex"} // must be "Jacob and Alex like this"
        likes {"Max", "John", "Mark"} // must be "Max, John and Mark like this"
        likes {"Alex", "Jacob", "Mark", "Max"} // must be "Alex, Jacob and 2 others like this"

        For 4 or more names, the number in and 2 others simply increases.
*/

/*
public class Solution {
    public static String whoLikesIt(String... names) {
        var sb = new StringBuilder();
        switch (names.length) {
            case 0 -> sb.append("no one likes this");
            case 1 -> sb.append(names[0]).append(" likes this");
            case 2 -> sb.append(names[0]).append(" and ").append(names[1]).append(" like this");
            case 3 -> sb.append(names[0]).append(", ").append(names[1]).append(" and ").append(names[2]) .append(" like this");
            default -> sb.append(names[0]).append(", ").append(names[1]).append(" and ").append(names.length - 2) .append(" others like this");
        }
        return sb.toString();
    }
}*/
public class Solution {
    public static String whoLikesIt(String... names) {
        switch (names.length) {
            case 0: return "no one likes this";
            case 1: return String.format("%s likes this", names[0]);
            case 2: return String.format("%s and %s like this", names[0], names[1]);
            case 3: return String.format("%s, %s and %s like this", names[0], names[1], names[2]);
            default: return String.format("%s, %s and %d others like this", names[0], names[1], names.length - 2);
        }
    }
}

/*
public class Solution {
    public static String whoLikesIt(String... names) {
        var sb = new StringBuilder();
        switch (names.length) {
            case 0:
                sb.append("no one likes this");
                break;
            case 1:
                sb.append(names[0]).append(" likes this");
                break;
            case 2:
                sb.append(names[0]).append(" and ").append(names[1]).append(" like this");
                break;
            case 3:
                sb.append(names[0]).append(", ").append(names[1]).append(" and ").append(names[2]).append(" like this");
                break;
            default:
                sb.append(names[0]).append(", ").append(names[1]).append(" and ").append(names.length - 2).append(" others like this");
        }
        return sb.toString();
    }
}
*/
