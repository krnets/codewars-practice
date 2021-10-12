#pragma once

#include <range/v3/all.hpp>

using namespace ranges;

using std::vector;

/*
vector<std::pair<int, int>> twos_difference(const vector<int>& vec)
{
	std::set<int> set(vec.begin(), vec.end());

	return set
		| views::filter([&](int x) { return set.count(x + 2) != 0; })
		| views::transform([](int x) { return std::make_pair(x, x + 2); })
		| to<vector<std::pair<int, int>>>();
}
*/

/*
vector<std::pair<int, int>> twos_difference(const vector<int>& vec)
{
	std::set<int> set(vec.begin(), vec.end());

	return set
		| views::remove_if([&](int x) { return set.count(x + 2) == 0; })
		| views::transform([](int x) { return std::make_pair(x, x + 2); })
		| to<vector<std::pair<int, int>>>();
}
*/

vector<std::pair<int, int>> twos_difference(const vector<int>& vec)
{
	std::set<int> set(vec.begin(), vec.end());
	vector<std::pair<int, int>> result;

	for (int x : set)
		if (set.count(x + 2))
			result.emplace_back(std::make_pair(x, x + 2));

	return result;
}
