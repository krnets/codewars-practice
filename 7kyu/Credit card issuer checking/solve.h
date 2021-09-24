#pragma once

std::string getIssuer(const std::string& number)
{
	if (number[0] == '4' && (number.length() == 13 || number.length() == 16))
		return "VISA";

	if (number.substr(0, 4) == "6011" && number.length() == 16)
		return "Discover";

	std::string sub = number.substr(0, 2);

	if (number.length() == 15 && (sub == "34" || sub == "37"))
		return "AMEX";

	if (number.length() == 16 && (sub == "51" || sub == "52" || sub == "53" || sub == "54" || sub == "55"))
		return "Mastercard";

	return "Unknown";
}
