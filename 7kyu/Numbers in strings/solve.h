#pragma once

#include <numeric>
#include <regex>

using namespace std;

/*
int solve(string s)
{
	int ans = 0;
	regex re("\\d+");
	auto it = sregex_token_iterator(s.begin(), s.end(), re);

	while (it != sregex_token_iterator())
	{
		ans = max<int>(ans, stoi(it->str()));
		++it;
	}

	return ans;
}
*/

/*
int solve(string s)
{
	int ans = 0;
	regex re("\\d+");
	auto begin = sregex_iterator(s.begin(), s.end(), re);

	for_each(begin, {}, [&](auto m) { ans = max(ans, stoi(m.str())); });

	return ans;
}
*/

int solve(string s)
{
	regex re("\\d+");
	auto begin = sregex_token_iterator(s.begin(), s.end(), re);

	return accumulate(begin, {}, 0,
	                  [](auto ans, auto match) { return max(ans, stoi(match)); });
}
