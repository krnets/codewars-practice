#pragma once
#include <range/v3/algorithm/find.hpp>
#include <range/v3/numeric/iota.hpp>

using namespace ranges;

int solve(int n, int k)
{
	std::vector<int> nums(n);
	iota(nums, 0);

	for (int i = 0; i < n; ++i)
	{
		reverse(nums.begin() + i, nums.end());
	}

	return find(nums, k) - nums.begin();
}
