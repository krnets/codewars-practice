#pragma once
#include <numeric>
#include <set>
#include <range/v3/action/sort.hpp>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/all.hpp>
#include <range/v3/view/unique.hpp>

/*
int solve(std::vector<int> v)
{
	std::set s(v.begin(), v.end());

	return ranges::accumulate(s, 0);
}
*/

/*
int solve(std::vector<int> v)
{
	std::sort(v.begin(), v.end());

	return std::accumulate(v.begin(), std::unique(v.begin(), v.end()), 0);
}
*/

using namespace ranges;

/*
int solve(std::vector<int> v)
{
	sort(v);

	return accumulate(v | views::unique, 0);
}
*/

int solve(std::vector<int> v)
{
	return accumulate(v | views::all | actions::sort | views::unique, 0);
}
