#pragma once

#include <range/v3/view/iota.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::vector;

/*
vector<vector<int>> pyramid(std::size_t n)
{
	vector<vector<int>> res;

	for (size_t i = 1; i <= n; ++i)
	{
		vector v(i, 1);
		res.push_back(v);
	}

	return res;
}
*/

vector<vector<int>> pyramid(std::size_t n)
{
	if (n == 0) return vector<vector<int>>();

	return views::closed_iota(1, int(n))
		| views::transform([](int i) { return vector(i, 1); })
		| to<vector<vector<int>>>();
}
