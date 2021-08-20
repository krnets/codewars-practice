#include <string>
#include <vector>
#include <algorithm>

/*
std::string twoSort(std::vector<std::string> s)
{
	std::sort(s.begin(), s.end(), std::greater<>());
	std::string word = s.back();

	std::string ans;

	for (const char& c : word)
	{
		ans += c;
		ans += "***";
	}

	return ans.substr(0, ans.size() - 3);
}
*/

std::string twoSort(std::vector<std::string> s)
{
	std::sort(s.begin(), s.end());
	std::string word = s.front();

	for (int i = 1; i < word.size(); i += 4)
	{
		word.insert(i, "***");
	}

	return word;
}
