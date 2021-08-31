#pragma once
#include <regex>

/*
std::vector<int> vowelIndices(const std::string& word)
{
	std::vector<int> res;
	std::string vowels = "aeiouy";

	for (int i = 0; i < word.size(); ++i)
		if (vowels.find(::tolower(word.at(i))) != std::string::npos)
			res.push_back(i + 1);

	return res;
}
*/

std::vector<int> vowelIndices(const std::string& word)
{
	std::vector<int> res;

	for (int i = 0; i < word.size(); ++i)
		switch (::toupper(word[i]))
		{
		case 'A':
		case 'E':
		case 'I':
		case 'O':
		case 'U':
		case 'Y':
			res.push_back(i + 1);
		default: ;
		}

	return res;
}


/*
std::vector<int> vowelIndices(const std::string& word)
{
	std::vector<int> v;
	std::regex re("[aeiouy]", std::regex::icase);

	for (int i = 0; i < word.size(); ++i)
		if (std::regex_match(word.substr(i, 1), re))
			v.push_back(i + 1);

	return v;
}
*/
