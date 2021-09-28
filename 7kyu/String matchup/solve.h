#pragma once

using std::vector;
using std::string;

/*
vector<int> solve(vector<string> a, vector<string> b)
{
	vector<int> vec;

	for (auto s : b)
	{
		int count = 0;

		for (auto t : a)
			if (s == t)
				count++;

		vec.push_back(count);
	}

	return vec;
}
*/

/*
vector<int> solve(vector<string> a, vector<string> b)
{
	vector<int> vec(b.size());

	for (int i = 0; i < b.size(); ++i)
	{
		vec[i] = std::count(a.begin(), a.end(), b[i]);
	}

	return vec;
}
*/

#include <range/v3/algorithm/count.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

vector<int> solve(vector<string> a, vector<string> b)
{
	return b
		| ranges::views::transform([a](auto x) { return ranges::count(a, x); })
		| ranges::to<vector<int>>();
}
