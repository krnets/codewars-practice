# 7kyu - Currency Conversion

""" You are currently in the United States of America. 
The main currency here is known as the United States Dollar (USD). 
You are planning to travel to another country for vacation, so you make it today's goal 
to convert your USD (all bills, no cents) into the appropriate currency. 
This will help you be more prepared for when you arrive in the country you will be vacationing in.

Given an integer (usd) representing the amount of dollars you have and a string (currency) 
representing the name of the currency used in another country, it is your task to determine the amount 
of foreign currency you will receive when you exchange your United States Dollars.

However, there is one minor issue to deal with first. The screens and monitors at the Exchange are messed up. 
Some conversion rates are correctly presented, but other conversion rates are incorrectly presented. 
For some countries, they are temporarily displaying the standard conversion rate 
in the form of a number's binary representation!

You make some observations. If a country's currency begins with a vowel, then the conversion rate is unaffected 
by the technical difficulties. If a country's currency begins with a consonant, then the conversion rate has been tampered with.

Normally, the display would show 1 USD converting to 111 Japanese Yen. 
Instead, the display is showing 1 USD converts to 1101111 Japanese Yen. 
You take it upon yourself to sort this out. By doing so, your 250 USD rightfully becomes 27750 Japanese Yen.

function(250, "Japanese Yen") => "You now have 27750 of Japanese Yen."

Normally, the display would show 1 USD converting to 21 Czech Koruna. 
Instead, the display is showing 1 USD converts to 10101 Czech Koruna. 
You take it upon yourself to sort this out. 
By doing so, your 325 USD rightfully becomes 6825 Czech Koruna.

function(325, "Czech Koruna") => "You now have 6825 of Czech Koruna."

Using your understanding of converting currencies in conjunction with the preloaded conversion-rates table, 
properly convert your dollars into the correct amount of foreign currency. """

CONVERSION_RATES = {
    "Argentinian Peso": 10,
    "Armenian Dram": 478,
    "Bangladeshi Taka": 1010010,
    "Croatian Kuna": 110,
    "Czech Koruna": 10101,
    "Dominican Peso": 110000,
    "Egyptian Pound": 18,
    "Guatemalan Quetzal": 111,
    "Haitian Gourde": 1000000,
    "Indian Rupee": 63,
    "Japanese Yen": 1101111,
    "Kenyan Shilling": 1100110,
    "Nicaraguan Cordoba": 11111,
    "Norwegian Krone": 1000,
    "Philippine Piso": 110010,
    "Romanian Leu": 100,
    "Samoan Tala": 11,
    "South Korean Won": 10000100011,
    "Thai Baht": 100000,
    "Uzbekistani Som": 8333,
    "Venezuelan Bolivar": 1010,
    "Vietnamese Dong": 101100000101101
}

# def convert_my_dollars(usd, currency):
#     new_amout = 0
#     if currency[0] in '[AEIOU]':
#         new_amout = CONVERSION_RATES[currency] * usd
#     else:
#         new_amout = int(str(CONVERSION_RATES[currency]), 2) * usd
#     return f'You now have {new_amout} of {currency}.'

# def convert_my_dollars(usd, currency):
#     amount = CONVERSION_RATES[currency] * usd if currency[0] in '[AEIOU]' else int(str(CONVERSION_RATES[currency]), 2) * usd
#     return f'You now have {amount} of {currency}.'

# def convert_my_dollars(usd, currency):
#     rate = CONVERSION_RATES[currency] if currency[0] in '[AEIOU]' else int(str(CONVERSION_RATES[currency]), 2)
#     return f'You now have {usd * rate} of {currency}.'

def convert_my_dollars(usd, currency):
    base = 10 if currency[0] in '[AEIOU]' else 2
    rate = int(str(CONVERSION_RATES[currency]), base)
    return f'You now have {usd * rate} of {currency}.'


q = convert_my_dollars(7, "Armenian Dram"), "You now have 3346 of Armenian Dram."
q
q = convert_my_dollars(322, "Armenian Dram"), "You now have 153916 of Armenian Dram."
q
q = convert_my_dollars(25, "Bangladeshi Taka"), "You now have 2050 of Bangladeshi Taka."
q
q = convert_my_dollars(730, "Bangladeshi Taka"), "You now have 59860 of Bangladeshi Taka."
q
q = convert_my_dollars(37, "Croatian Kuna"), "You now have 222 of Croatian Kuna."
q
q = convert_my_dollars(40, "Croatian Kuna"), "You now have 240 of Croatian Kuna."
q
q = convert_my_dollars(197, "Czech Koruna"), "You now have 4137 of Czech Koruna."
q
q = convert_my_dollars(333, "Czech Koruna"), "You now have 6993 of Czech Koruna."
q
q = convert_my_dollars(768, "Dominican Peso"), "You now have 36864 of Dominican Peso."
q
q = convert_my_dollars(983, "Dominican Peso"), "You now have 47184 of Dominican Peso."
q
