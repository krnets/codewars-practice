#pragma once

#include <unordered_set>

std::string removeDuplicateWords(const std::string& str)
{
	std::unordered_set<std::string> wordSeen;
	std::istringstream iss(str);
	std::string word;
	std::string result;

	while (iss >> word)
	{
		// if (set.count(word) == 0)
		if (wordSeen.find(word) == wordSeen.end())
			result.append(word).append(" ");

		wordSeen.insert(word);
	}

	// return result.substr(0, result.size() - 1);
	result.pop_back();

	return result;
}
