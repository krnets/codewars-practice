/*
Kate and Michael want to buy a pizza and share it.
Depending on the price of the pizza, they are going to divide the costs:

If the pizza is less than €5,- Michael invites Kate, so Michael pays the full price.
Otherwise Kate will contribute 1/3 of the price, but no more than €10 (she's broke :-)
and Michael pays the rest.

How much is Michael going to pay? Calculate the amount with two decimals, if necessary.
*/

/*
import java.math.BigDecimal;
import java.math.RoundingMode;

public class PizzaPayments {
    public static double michaelPays(double cost) {
        var amount = 0D;
        if (cost <= 5) {
            amount = Math.round(100 * cost) / 100D;
        } else if (cost <= 30) {
            amount = Math.round(100 * (cost * 2 / 3)) / 100D;
        } else {
            amount = Math.round(100 * cost) / 100D - 10;
        }
        var res = new BigDecimal(Double.toString(amount)).setScale(2, RoundingMode.HALF_UP);
        return Double.parseDouble(String.valueOf(res));
    }
}
*/

public class PizzaPayments {
    public static double michaelPays(double cost) {
        return Math.round((cost < 5 ? cost : cost - Math.min(cost / 3, 10)) * 100) / 100.0;
    }
}