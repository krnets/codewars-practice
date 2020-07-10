public class Ghost {
    public String getColor() {
        return new String[]{"white", "yellow", "purple", "red"}[(int) Math.floor(Math.random() * 4)];
    }
}