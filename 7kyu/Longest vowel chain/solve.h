#pragma once
#include <regex>

using namespace std;

/*
int solve(string s)
{
	int ans = 0;
	regex re("([^aeiou]+)", regex::icase);
	vector<string> v;

	copy(sregex_token_iterator(s.begin(), s.end(), re, -1),
	     sregex_token_iterator(),
	     back_inserter(v));

	for (const string& vowel_chain : v)
		if (ans < vowel_chain.length())
			ans = vowel_chain.length();

	return ans;
}
*/

/*
int solve(string s)
{
	int ans = 0;
	regex re("([aeiou]+)", regex::icase);
	vector<string> v;

	copy(sregex_token_iterator(s.begin(), s.end(), re),
	     sregex_token_iterator(),
	     back_inserter(v));

	for (auto vowel_chain : v)
		ans = max<int>(ans, vowel_chain.length());

	return ans;
}
*/

int solve(string s)
{
	int ans = 0;
	regex re("[aeiou]+", regex::icase);
	auto begin = sregex_token_iterator(s.begin(), s.end(), re);

	for (auto it = begin; it != sregex_token_iterator(); ++it)
		ans = max<int>(ans, it->length());

	return ans;
}
