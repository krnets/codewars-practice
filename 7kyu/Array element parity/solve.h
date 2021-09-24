#pragma once
#include <numeric>
#include <range/v3/numeric/accumulate.hpp>
#include <set>

/*
int solve(std::vector<int> v)
{
	std::set s(v.begin(), v.end());

	return ranges::accumulate(s, 0);
}
*/

int solve(std::vector<int> v)
{
	std::sort(v.begin(), v.end());

	return std::accumulate(v.begin(), std::unique(v.begin(), v.end()), 0);
}
