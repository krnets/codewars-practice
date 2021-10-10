#pragma once

// #include <range/v3/all.hpp>
#include <range/v3/view/iota.hpp>
#include <range/v3/view/repeat.hpp>
#include <range/v3/view/take.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::vector;

/*
vector<vector<int>> multiplication_table(int n)
{
	vector<vector<int>> v;

	for (int i = 1; i <= n; ++i)
	{
		vector<int> row(n);

		for (int j = 1; j <= n; ++j)
		{
			row[j - 1] = i * j;
		}
		v.push_back(row);
	}

	return v;
}
*/

/*
vector<vector<int>> multiplication_table(int n)
{
	vector<vector<int>> result;
	auto series = views::iota(1, n + 1) | to<vector<int>>();
	auto rng = views::repeat(series) | views::take(n);

	for (auto vec : rng)
	{
		for (int& x : vec) x *= n;

		result.insert(result.begin(), vec);
		--n;
	}
	return result;
}
*/

/*
vector<vector<int>> multiplication_table(int n)
{
	vector<vector<int>> result;
	auto series = views::iota(1, n + 1) | to<vector<int>>();

	for (auto vec : views::repeat(series) | views::take(n))
	{
		for (int& x : vec) x *= n;

		result.insert(result.begin(), vec);
		--n;
	}
	return result;
}
*/

vector<vector<int>> multiplication_table(int n)
{
	vector<vector<int>> result;
	auto series = views::closed_iota(1, n) | to<vector<int>>();

	for (auto vec : views::repeat(series) | views::take(n))
	{
		for (int& x : vec) x *= n;

		result.insert(result.begin(), vec);
		--n;
	}
	return result;
}
