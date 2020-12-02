import java.util.Objects;

public class Cat implements Comparable<Cat> {
    public String name;
    public double weight;

    public Cat(String name, double weight) {
        this.name = name;
        this.weight = weight;
    }

    @Override
    public int compareTo(Cat c) {
        return this.name.compareTo(c.name);
    }

    @Override
    public boolean equals(Object o) {
        if (!(o instanceof Cat)) return false;
        Cat other = (Cat) o;

        return Double.compare(this.weight, other.weight) == 0 && Objects.equals(this.name, other.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, weight);
    }
}
