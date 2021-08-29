#pragma once

/*
std::string solve(const std::string& str)
{
	int countLower = std::count_if(str.begin(), str.end(), [](char c) { return c >= 'a' && c <= 'z'; });
	std::string ret(str);

	if (countLower >= (str.length() + 1) / 2)
		std::transform(ret.begin(), ret.end(), ret.begin(), [](char c) { return ::tolower(c); });
	else
		std::transform(ret.begin(), ret.end(), ret.begin(), [](char c) { return ::toupper(c); });

	return ret;
}
*/

std::string solve(const std::string& str)
{
	std::string ret(str);
	bool b_lower = str.size() <= 2 * std::count_if(str.begin(), str.end(), [](char c) { return ::islower(c); });

	std::transform(ret.begin(), ret.end(), ret.begin(),
	               [b_lower](char c) { return b_lower ? ::tolower(c) : toupper(c); });

	return ret;
}
