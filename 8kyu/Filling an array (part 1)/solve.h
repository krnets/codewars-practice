#pragma once
#include <numeric>

#include <range/v3/view/iota.hpp>
#include <range/v3/to_container.hpp>

using std::vector;

/*
std::vector<int> arr(int n = 0)
{
	std::vector<int> vec(n);
	std::iota(vec.begin(), vec.end(), 0);

	return vec;
}
*/

vector<int> arr(int n = 0)
{
	return ranges::views::iota(0, n)
		| ranges::to<vector<int>>();
}
