#pragma once
#include <regex>

using std::string;

string alphabetWar(string fight)
{
	std::map<char, int> cpower{
		{'w', -4}, {'p', -3}, {'b', -2}, {'s', -1},
		{'m', 4}, {'q', 3}, {'d', 2}, {'z', 1}
	};
	int score = 0;
	string post_strike;
	std::regex re("(.?\\*+.?)");
	std::regex_replace(std::back_inserter(post_strike), fight.begin(), fight.end(), re, "");

	for (char c : post_strike)
		if (cpower.find(c) != cpower.end())
			score += cpower[c];

	return score < 0 ? "Left side wins!" : score > 0 ? "Right side wins!" : "Let's fight again!";
}
