#pragma once
#include <string>
#include <sstream>

int find_short(std::string str)
{
	size_t ans = std::numeric_limits<int>::max();
	std::istringstream iss(str);
	std::string word;

	while (iss >> word)
	{
		ans = std::min(ans, word.size());
	}

	return ans;
}
