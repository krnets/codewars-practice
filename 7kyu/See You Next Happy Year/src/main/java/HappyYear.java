public class HappyYear {
    static public int nextHappyYear(int year) {
        while (String.valueOf(++year).chars().distinct().count() != 4) ;
        return year;
    }
}