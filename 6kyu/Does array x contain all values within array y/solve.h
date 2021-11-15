#pragma once
#include <unordered_set>
#include <range/v3/algorithm/all_of.hpp>

using std::vector;

/*
bool contains_all(const vector<int>& arr, const vector<int>& target)
{
	std::unordered_set set(arr.begin(), arr.end());

	for (int x : target)
		if (!set.count(x))
			return false;

	return true;
}
*/

bool contains_all(const vector<int>& arr, const vector<int>& target)
{
	std::unordered_set set(arr.begin(), arr.end());

	return ranges::all_of(target, [set](int x) { return set.count(x) > 0; });
}
