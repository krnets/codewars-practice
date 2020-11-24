import java.util.ArrayList;

public class Metro {

    public static int countPassengers(ArrayList<int[]> stops) {
        int passengersOnBus = 0;

        for (int[] stop : stops) {
            passengersOnBus -= stop[1];

            if (passengersOnBus < 0) {
                throw new RuntimeException("number of remaining passengers cannot be less than 0");
            }
            passengersOnBus += stop[0];
        }
        return passengersOnBus;
    }
}
