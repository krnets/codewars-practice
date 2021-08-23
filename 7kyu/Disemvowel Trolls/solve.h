#pragma once
#include <regex>
#include <string>

std::string disemvowel(const std::string& str)
{
	std::string vowels = "aeiou";
	std::regex re("[" + vowels + "]", std::regex_constants::icase);

	return std::regex_replace(str, re, "");
}
