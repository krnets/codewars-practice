#pragma once

#include <numeric>
#include <set>

/*
unsigned long long minValue(std::vector<int> values)
{
	std::set<int> s(values.begin(), values.end());

	unsigned long long ans = 0;

	for (auto it = s.begin(); it != s.end(); ++it)
	{
		ans = (ans * 10) + *it;
	}

	return ans;
}
*/

unsigned long long minValue(std::vector<int> values)
{
	std::set<int> digits(values.begin(), values.end());

	return std::accumulate(digits.begin(), digits.end(), 0ull, [](int x, int y) { return 10 * x + y; });
}
