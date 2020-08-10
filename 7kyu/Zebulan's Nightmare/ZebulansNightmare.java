/*
Zebulan has worked hard to write all his python code in strict compliance to PEP8 rules.
In this kata, you are a mischevious hacker that has set out to sabatoge all his good code.

Your job is to take PEP8 compatible function names and convert them to camelCase. For example:

        zebulansNightmare('camel_case') == 'camelCase'
        zebulansNightmare('zebulans_nightmare') == 'zebulansNightmare'
        zebulansNightmare('get_string') == 'getString'
        zebulansNightmare('convert_to_uppercase') == 'convertToUppercase'
        zebulansNightmare('main') == 'main'
*/

/*
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class ZebulansNightmare {
    public static String zebulansNightmare(final String functionName) {
        String[] names = functionName.split("_");
        return names[0].concat(IntStream.range(1, names.length)
                .mapToObj(i -> Character.toUpperCase(names[i].charAt(0)) + names[i].substring(1))
                .collect(Collectors.joining()));
    }
}*/

/*
public class ZebulansNightmare {
    public static String zebulansNightmare(final String functionName) {
        int pos = functionName.indexOf("_");
        return pos == -1 ? functionName : zebulansNightmare(functionName
                .replaceFirst("_(.)", String.valueOf(functionName.charAt(pos + 1)).toUpperCase()));
    }
}
*/

public class ZebulansNightmare {
    public static String zebulansNightmare(final String functionName) {
        var names = functionName.split("_");
        var sb = new StringBuilder().append(names[0]);
        for (int i = 1; i < names.length; i++) {
            sb.append(names[i].substring(0, 1).toUpperCase()).append(names[i].substring(1));
        }
        return sb.toString();
    }
}
