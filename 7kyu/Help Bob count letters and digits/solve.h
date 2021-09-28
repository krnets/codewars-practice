#pragma once

/*
int countLettersAndDigits(std::string input)
{
	return std::ranges::count_if(input, [](char c) { return isdigit(c) || isalpha(c); });
}
*/

int countLettersAndDigits(std::string input)
{
	return std::ranges::count_if(input, isalnum);
}
