/*
Complete the function getIssuer() that will use the values shown below to determine the card issuer for
a given card number. If the number cannot be matched then the function should return the string Unknown.

        | Card Type  | Begins With          | Number Length |
        |------------|----------------------|---------------|
        | AMEX       | 34 or 37             | 15            |
        | Discover   | 6011                 | 16            |
        | Mastercard | 51, 52, 53, 54 or 55 | 16            |
        | VISA       | 4                    | 13 or 16      |

        Examples

        getIssuer(4111111111111111) == "VISA"
        getIssuer(4111111111111) == "VISA"
        getIssuer(4012888888881881) == "VISA"
        getIssuer(378282246310005) == "AMEX"
        getIssuer(6011111111111117) == "Discover"
        getIssuer(5105105105105100) == "Mastercard"
        getIssuer(5105105105105106) == "Mastercard"
        getIssuer(9111111111111111) == "Unknown"
*/

/*
public class Kata {
    public static String getIssuer(String cardNumber) {
        return cardNumber.matches("^3(4|7)[0-9]{13}$") ? "AMEX" :
               cardNumber.matches("^6011[0-9]{12}$") ? "Discover" :
               cardNumber.matches("^5[1-5][0-9]{14}$") ? "Mastercard" :
               cardNumber.matches("^4([0-9]{12}|[0-9]{15})") ? "VISA" : "Unknown";
    }
}*/

public class Kata {
    public static String getIssuer(String cardNumber) {
        return cardNumber.matches("^3(4|7)\\d{13}$") ? "AMEX" :
               cardNumber.matches("^6011\\d{12}$") ? "Discover" :
               cardNumber.matches("^5[1-5]\\d{14}$") ? "Mastercard" :
               cardNumber.matches("^4(\\d{12}|\\d{15})") ? "VISA" : "Unknown";
    }
}

