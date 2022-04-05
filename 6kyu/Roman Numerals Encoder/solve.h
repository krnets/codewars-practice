#pragma once
#include <string>

std::string solution(int number)
{
	std::string result;
	std::map<int, std::string> map_to_roman{
		{1, "I"}, {4, "IV"}, {5, "V"}, {9, "IX"},
		{10, "X"}, {40, "XL"}, {50, "L"}, {90, "XC"},
		{100, "C"}, {400, "CD"}, {500, "D"}, {900, "CM"},
		{1000, "M"},
	};

	for (auto it = map_to_roman.rbegin(); it != map_to_roman.rend(); ++it)
	{
		int decimal = it->first;
		auto roman_symbol = it->second;

		while (number >= decimal)
		{
			result += roman_symbol;
			number -= decimal;
		}
	}

	return result;
}
