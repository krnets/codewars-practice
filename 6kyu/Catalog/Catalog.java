/*
You are given a small extract of a catalog:

        s = "<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>

        <prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>

        <prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>

        <prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>

        <prod><name>saw</name><prx>9</prx><qty>10</qty></prod>

        ...

        (prx stands for price, qty for quantity) and an article i.e "saw".

        The function catalog(s, "saw") returns the line(s) corresponding
        to the article with $ before the prices:

        "table saw > prx: $1099.99 qty: 5\n
        saw > prx: $9 qty: 10\n..."

        If the article is not in the catalog return "Nothing".

Notes:  There is a blank line between two lines of the catalog.
        The same article may appear more than once. If that happens
        return all the lines concerned by the article
        (in the same order as in the catalog).
        The line separator of results may depend on the language \nor \r\n.
        You can see examples in the "Sample tests".
*/

import java.util.ArrayList;
import java.util.Arrays;

public class Catalog {
    public static String catalog(String s, String article) {
        var linesWithArticle = Arrays.stream(s.split("\\n"))
//                .filter(x -> x.indexOf(article) > 0)
                .filter(str -> str.contains(article))
                .toArray(String[]::new);

        var linesFormatted = new ArrayList<String>();

        String nameTag = "<name>", prxTag = "<prx>", qtyTag = "<qty>";

        for (var line : linesWithArticle) {
            var name = line.substring(line.indexOf(nameTag) + nameTag.length(), line.indexOf("</name>"));
            var prx = line.substring(line.indexOf(prxTag) + prxTag.length(), line.indexOf("</prx>"));
            var qty = line.substring(line.indexOf(qtyTag) + qtyTag.length(), line.indexOf("</qty>"));

            linesFormatted.add(String.format("%s > prx: $%s qty: %s", name, prx, qty));
        }
        return linesFormatted.isEmpty() ? "Nothing" : String.join("\n", linesFormatted);
    }
}
