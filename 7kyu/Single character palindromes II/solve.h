#pragma once

// #include <range/v3/all.hpp>
//
// using namespace ranges;
// using std::vector;
// using std::string;

bool solve(std::string s)
{
	int count = 0, n = s.length();

	for (int i = 0; i < n; ++i)
		if (s[i] == s[n - i - 1])
			++count;

	return count == n && (n & 1) || count == n - 2;
}
