#pragma once

/*
bool tidyNumber(int number)
{
	std::string digits = std::to_string(number);
	char prev_ch = digits.front();

	for (int i = 1; i < digits.length(); ++i)
	{
		char curr_ch = digits[i];

		if (prev_ch > curr_ch)
			return false;

		prev_ch = curr_ch;
	}

	return true;
}
*/

/*
bool tidyNumber(int number)
{
	int last = number % 10;

	while (number > 0)
	{
		int curr = number % 10;

		if (last < curr)
			return false;

		last = curr;
		number /= 10;
	}
	return true;
}
*/

#include <range/v3/algorithm/is_sorted.hpp>

bool tidyNumber(int number)
{
	std::string digits = std::to_string(number);

	return ranges::is_sorted(digits);
}
