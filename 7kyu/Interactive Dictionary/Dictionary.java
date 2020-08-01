/*
In this kata, your job is to create a class Dictionary which you can add words to and their entries.
Example:
        >>> Dictionary d = new Dictionary();
        >>> d.newEntry("Apple", "A fruit that grows on trees");
        >>> System.out.println(d.look("Apple"));
        A fruit that grows on trees
        >>> System.out.println(d.look("Banana"));
        Cant find entry for Banana
*/

import java.util.HashMap;
import java.util.Map;

/*
public class Dictionary {
    private Map dict = new HashMap<String, String>();

    public Dictionary() {
    }

    public void newEntry(String key, String value) {
        dict.put(key, value);
    }

    public String look(String key) {
//        return dict.containsKey(key) ? String.valueOf(dict.get(key)) : "Cant find entry for " + key;
        return String.valueOf(dict.getOrDefault(key, "Cant find entry for " + key));
    }
}*/

public class Dictionary extends HashMap<String, String> {
    public Dictionary() {
        super();
    }

    public void newEntry(String key, String value) {
        this.put(key, value);
    }

    public String look(String key) {
        return this.getOrDefault(key, "Cant find entry for " + key);
    }
}
