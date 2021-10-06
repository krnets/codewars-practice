#pragma once

#include <regex>

using std::string;

/*
string to_camel_case(string text)
{
	string ans;
	bool capital = false;

	for (char c : text)
	{
		if (!isalpha(c))
			capital = true;
		else if (capital || isupper(c))
		{
			ans.push_back(toupper(c));
			capital = false;
		}
		else ans.push_back(tolower(c));
	}

	return ans;
}
*/

string to_camel_case(string text)
{
	std::regex re("([-_])");
	auto it = std::sregex_token_iterator(text.begin(), text.end(), re, -1);
	string ans = it->str();

	for_each(++it, {}, [&](auto m)
	{
		string word = m.str();
		word[0] = toupper(word[0]);
		ans.append(word);
	});

	return ans;
}
