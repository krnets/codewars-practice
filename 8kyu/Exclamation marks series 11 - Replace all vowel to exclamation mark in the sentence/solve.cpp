#include <regex>
#include <string>

/*
std::string replace(const std::string& s)
{
	std::string result;
	std::string vowels = "aeiouAEIOU";

	for (char c : s)
	{
		if (vowels.find(c, 0) != std::string::npos)
			result += '!';
		else
			result += c;
	}

	return result;
}
*/


std::string replace(const std::string& s)
{
	const char* vowels = "[aeiouAEIOU]";
	std::regex re = std::regex(vowels);
	return std::regex_replace(s, re, "!");
}

/*
std::string replace(const std::string& s)
{
	return regex_replace(s, std::regex("[aeiouAEIOU]"), "!");
}
*/
