#include <sstream>
#include <string>
#include <regex>

/*
bool is_digit(std::string s)
{
	std::string pattern = R"(^-?\d+\.?\d*$)";
	std::regex re(pattern);

	return std::regex_match(s, re);
}
*/

bool is_digit(std::string s)
{
	std::istringstream iss(s);
	double checker;
	iss >> std::noskipws >> checker;

	return iss && iss.eof();
}
