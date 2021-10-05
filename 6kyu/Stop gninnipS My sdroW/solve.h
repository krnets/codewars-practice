#pragma once

using std::string;

string spinWords(const string& str)
{
	std::vector<string> words;
	std::istringstream iss(str);
	std::ostringstream oss;
	string word;

	while (iss >> word)
	{
		if (word.length() >= 5)
			reverse(word.begin(), word.end());

		oss << word << ' ';
	}
	string ans = oss.str();
	ans.pop_back();

	return ans;
}
