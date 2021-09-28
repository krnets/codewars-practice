#pragma once

#include <regex>
#include <string>

/*
int sum_of_a_beach(std::string s)
{
	std::regex re("(Sand)|(Water)|(Fish)|(Sun)", std::regex::icase);
	auto it = std::sregex_token_iterator(s.begin(), s.end(), re);
	int count = 0;

	while (it != std::sregex_token_iterator())
	{
		++count;
		++it;
	}

	return count;
}
*/

int sum_of_a_beach(std::string s)
{
	std::regex re("sand|water|fish|sun", std::regex::icase);
	auto it = std::sregex_token_iterator(s.begin(), s.end(), re);

	return std::distance(it, {});
}
