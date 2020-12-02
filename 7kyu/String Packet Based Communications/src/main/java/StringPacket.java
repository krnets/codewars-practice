import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class StringPacket {

    public static String communicationModule(String packet) {
        List<String> list = Pattern.compile("(?<=\\G.{4})")
                .splitAsStream(packet)
                .collect(Collectors.toList());

        String header = list.get(0);
        String instruction = list.get(1);
        int data1 = Integer.parseInt(list.get(2));
        int data2 = Integer.parseInt(list.get(3));
        String footer = list.get(4);

        switch (instruction) {
            case "0F12":
                data1 = data1 + data2;
                break;
            case "B7A2":
                data1 = data1 - data2;
                break;
            case "C3D9":
                data1 = data1 * data2;
        }
        instruction = "FFFF";
        data1 = Math.max(0, data1);
        data1 = Math.min(9999, data1);
        data2 = 0;

        return String.format("%s%s%04d%04d%s", header, instruction, data1, data2, footer);
    }
}