#include <string>
#include <algorithm>

/*
std::string to_alternating_case(const std::string& str)
{
	std::string result;

	for (char c : str)
	{
		if (std::islower(c))
			result += std::toupper(c);

		else if (std::isupper(c))
			result += std::tolower(c);

		else result += c;
	}

	return result;
}
*/

/*
std::string to_alternating_case(const std::string& str)
{
	std::string result;

	for (char c : str)
	{
		result += std::isupper(c) ? std::tolower(c) : std::toupper(c);
	}

	return result;
}
*/

/*
std::string to_alternating_case(const std::string& str)
{
	std::string res{str};

	for (char& c : res)
		if (std::isalpha(c))
			c ^= (1 << 5);

	return res;
}
*/

std::string to_alternating_case(const std::string& str)
{
	std::string res = str;

	std::transform(res.begin(), res.end(), res.begin(),
	               [](char c) { return (std::isalpha(c) ? c ^ (1 << 5) : c); });

	return res;
}
