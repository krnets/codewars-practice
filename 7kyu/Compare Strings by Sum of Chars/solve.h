#pragma once
#include <numeric>

bool compare(std::string s1, std::string s2)
{
	auto f = [](char c) { return !isalpha(c); };
	auto g = [](int acc, char c) { return acc + toupper(c); };

	s1 = std::any_of(s1.begin(), s1.end(), f) ? "" : s1;
	s2 = std::any_of(s2.begin(), s2.end(), f) ? "" : s2;

	int sum1 = std::accumulate(s1.begin(), s1.end(), 0, g);
	int sum2 = std::accumulate(s2.begin(), s2.end(), 0, g);

	return sum1 == sum2;
}
