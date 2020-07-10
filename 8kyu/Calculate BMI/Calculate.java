/*
Write function bmi that calculates body mass index (bmi = weight / height ^ 2).

        if bmi <= 18.5 return "Underweight"
        if bmi <= 25.0 return "Normal"
        if bmi <= 30.0 return "Overweight"
        if bmi > 30 return "Obese"
*/
/*
public class Calculate {
    public static String bmi(double weight, double height) {
        double bodyMassIndex = weight / (height * height);
        if (bodyMassIndex <= 18.5)
            return "Underweight";
        if (bodyMassIndex <= 25.0)
            return "Normal";
        if (bodyMassIndex <= 30.0)
            return "Overweight";
        return "Obese";
    }
}
*/
public class Calculate {
    public static String bmi(double weight, double height) {
        return (weight /= Math.pow(height, 2)) > 30 ? "Obese" : weight > 25 ? "Overweight" : weight > 18.5 ? "Normal" : "Underweight";
    }
}
