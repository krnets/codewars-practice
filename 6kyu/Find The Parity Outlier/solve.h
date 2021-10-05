#pragma once

#include <range/v3/view/filter.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::vector;

int FindOutlier(std::vector<int> arr)
{
	auto is_even = [](int x) { return x % 2 == 0; };
	auto is_odd = [](int x) { return x % 2 != 0; };

	vector<int> evens = arr | views::filter(is_even) | to<vector<int>>();
	vector<int> odds = arr | views::filter(is_odd) | to<vector<int>>();

	return evens.size() == 1 ? evens.front() : odds.front();
}
