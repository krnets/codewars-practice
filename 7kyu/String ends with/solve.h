#pragma once

#include <string>

/*
bool solution(std::string const& str, std::string const& ending)
{
	if (ending.empty()) return true;
	if (ending.size() > str.size()) return false;

	int m = str.size();
	int n = ending.size();

	for (int i = 0; i < n; ++i)
		if (ending[n - i - 1] != str[m - i - 1])
			return false;

	return true;
}
*/

/*
bool solution(std::string const& str, std::string const& ending)
{
	return str.size() >= ending.size() && ending == str.substr(str.size() - ending.size());
}
*/

bool solution(std::string const& str, std::string const& ending)
{
	return std::equal(ending.rbegin(), ending.rend(), str.rbegin());
}
