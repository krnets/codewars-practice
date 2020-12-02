import java.util.Comparator;

public class CatWeightComparator implements Comparator<Cat> {

    /*
        @Override
        public int compare(Cat cat1, Cat cat2) {
            return Double.compare(cat1.weight, cat2.weight);
        }
    */
    @Override
    public int compare(Cat cat1, Cat cat2) {
        double result = cat1.weight - cat2.weight;
        return result < 0 ? -1 : result > 0 ? 1 : 0;
    }
}