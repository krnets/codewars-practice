#pragma once
#include <string>


int getCount(const std::string& inputStr)
{
	int num_vowels = 0;
	std::string vowels = "aeiou";

	for (char c : inputStr)
		if (vowels.find(c) != std::string::npos)
			num_vowels++;

	return num_vowels;
}
