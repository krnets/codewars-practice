#pragma once

#include <regex>
#include <range/v3/algorithm/count_if.hpp>

using std::regex;

/*
int countSmileys(std::vector<std::string> arr)
{
	int count = 0;

	regex re("[:;][-~]?[D)]");

	for (auto str : arr)
		if (regex_match(str.begin(), str.end(), re))
			count++;

	return count;
}
*/

/*
int countSmileys(std::vector<std::string> arr)
{
	int count = 0;

	regex re("[:;][-~]?[D)]");
	auto is_smiley = [&](auto str) { return regex_match(str.begin(), str.end(), re); };

	return std::count_if(arr.begin(), arr.end(), is_smiley);
}
*/

int countSmileys(std::vector<std::string> arr)
{
	regex re("[:;][-~]?[D)]");
	auto is_smiley = [&](auto str) { return regex_match(str.begin(), str.end(), re); };

	return ranges::count_if(arr, is_smiley);
}
