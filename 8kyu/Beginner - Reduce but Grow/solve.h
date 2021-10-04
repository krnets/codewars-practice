#pragma once

#include <numeric>
#include <range/v3/numeric/accumulate.hpp>

/*
int grow(std::vector<int> nums)
{
	return std::accumulate(nums.begin(), nums.end(), 1, [](int a, int b) { return a * b; });
}
*/


/*
int grow(std::vector<int> nums)
{
	return std::accumulate(nums.cbegin(), nums.cend(), 1, std::multiplies<int>());
}
*/

int grow(std::vector<int> nums)
{
	return ranges::accumulate(nums, 1, std::multiplies());
}
