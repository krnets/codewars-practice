#pragma once

#include <algorithm>

/*
std::string reverse_letter(const std::string &str)
{
	std::string reversed;

	for (int i = str.size() - 1; i >= 0; --i)
	{
		char c = str[i];

		if (::isalpha(c))
			reversed.push_back(c);
	}

	return reversed;
}
*/

/*
std::string reverse_letter(const std::string& str)
{
	std::string reversed;

	for (char c : str)
		if (::isalpha(c))
			reversed.insert(0, 1, c);

	return reversed;
}
*/

std::string reverse_letter(const std::string& str)
{
	std::string out(str.rbegin(), str.rend());
	out.erase(std::remove_if(out.begin(), out.end(), [](char c) { return !::isalpha(c); }), out.end());

	return out;
}
