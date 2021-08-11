/*#include <string>

std::string no_space(std::string s)
{
	std::string result;

	for (char c : s)
		if (c != ' ')
			result += c;

	return result;
}*/

/*#include <string>

std::string no_space(std::string s)
{
	std::string result;

	for (int i = 0; i < s.size(); ++i)
		if (s[i] != ' ')
			result += s[i];

	return result;
}*/

#include <regex>
#include <string>

std::string no_space(std::string s)
{
	return std::regex_replace(s, std::regex(" "), "");
}
