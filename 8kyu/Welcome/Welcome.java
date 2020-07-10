import java.util.HashMap;

/*
Your start-up's BA has told marketing that your website has a large audience in Scandinavia and surrounding countries.
Marketing thinks it would be great to welcome visitors to the site in their own language.
Luckily you already use an API that detects the user's location, so this is an easy win.

        The Task

Think of a way to store the languages as a database (eg an object).
The languages are listed below so you can copy and paste!

Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting -
if you have it in your database. It should default to English if the language is not in the database,
or in the event of an invalid input.

        The Database

        english: "Welcome",
        czech: "Vitejte",
        danish: "Velkomst",
        dutch: "Welkom",
        estonian: "Tere tulemast",
        finnish: "Tervetuloa",
        flemish: "Welgekomen",
        french: "Bienvenue",
        german: "Willkommen",
        irish: "Failte",
        italian: "Benvenuto",
        latvian: "Gaidits",
        lithuanian: "Laukiamas",
        polish: "Witamy",
        spanish: "Bienvenido",
        swedish: "Valkommen",
        welsh: "Croeso"

        Possible invalid inputs include:

        IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
        IP_ADDRESS_NOT_FOUND - ip address not in the database
        IP_ADDRESS_REQUIRED - no ip address was supplied
*/
/*
public class Welcome {
    public static String greet(String language) {
        HashMap<String, String> greetings = new HashMap();
        greetings.put("english", "Welcome");
        greetings.put("czech", "Vitejte");
        greetings.put("danish", "Velkomst");
        greetings.put("dutch", "Welkom");
        greetings.put("estonian", "Tere tulemast");
        greetings.put("finnish", "Tervetuloa");
        greetings.put("flemish", "Welgekomen");
        greetings.put("french", "Bienvenue");
        greetings.put("german", "Willkommen");
        greetings.put("irish", "Failte");
        greetings.put("italian", "Benvenuto");
        greetings.put("latvian", "Gaidits");
        greetings.put("lithuanian", "Laukiamas");
        greetings.put("polish", "Witamy");
        greetings.put("spanish", "Bienvenido");
        greetings.put("swedish", "Valkommen");
        greetings.put("welsh", "Croeso");
        return greetings.getOrDefault(language, "Welcome").toString();
    }
}
*/
public class Welcome {
    public static String greet(String language) {
        var greetings = new HashMap<String, String>();

        greetings.put("english", "Welcome");
        greetings.put("czech", "Vitejte");
        greetings.put("danish", "Velkomst");
        greetings.put("dutch", "Welkom");
        greetings.put("estonian", "Tere tulemast");
        greetings.put("finnish", "Tervetuloa");
        greetings.put("flemish", "Welgekomen");
        greetings.put("french", "Bienvenue");
        greetings.put("german", "Willkommen");
        greetings.put("irish", "Failte");
        greetings.put("italian", "Benvenuto");
        greetings.put("latvian", "Gaidits");
        greetings.put("lithuanian", "Laukiamas");
        greetings.put("polish", "Witamy");
        greetings.put("spanish", "Bienvenido");
        greetings.put("swedish", "Valkommen");
        greetings.put("welsh", "Croeso");

        return greetings.getOrDefault(language, "Welcome").toString();
    }
    }
