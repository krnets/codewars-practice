#pragma once

#include <unordered_map>

using std::string;

string wordPattern(const string& word)
{
	if (word.empty()) return word;

	std::ostringstream oss;
	std::unordered_map<char, int> map;
	int n = 0;

	for (char c : word)
	{
		c = tolower(c);

		if (map.find(c) == map.end())
		{
			map[c] = n;
			++n;
		}

		oss << map[c] << '.';
	}

	string ans = oss.str();
	ans.pop_back();

	return ans;
}
