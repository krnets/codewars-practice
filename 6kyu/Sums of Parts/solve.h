#pragma once

#include <numeric>
#include <range/v3/numeric/accumulate.hpp>

using std::vector;
using ULL = unsigned long long;

/*
vector<ULL> partsSum(const vector<ULL>& ls)
{
	vector<ULL> v(ls.size() + 1);
	ULL sum_left = 0, total = ranges::accumulate(ls, 0ull);

	for (int i = 0; i < ls.size(); i++)
	{
		v[i] = total - sum_left;
		sum_left += ls[i];
	}
	return v;
}
*/

/*
vector<ULL> partsSum(const vector<ULL>& ls)
{
	vector<ULL> sums(ls.size() + 1);
	sums[0] = ranges::accumulate(ls, 0ull);

	for (int i = 1; i < ls.size(); i++)
	{
		sums[i] = sums[i - 1] - ls[i - 1];
	}
	return sums;
}
*/

vector<ULL> partsSum(const vector<ULL>& ls)
{
	vector<ULL> sums(ls.size() + 1);
	ULL partial = 0;

	for (int i = ls.size() - 1; i >= 0; --i)
	{
		sums[i] += ls[i] + partial;
		partial += ls[i];
	}

	return sums;
}

/*
vector<ULL> partsSum(const vector<ULL>& ls)
{
	vector<ULL> v(ls.size() + 1);
	std::partial_sum(ls.rbegin(), ls.rend(), v.rbegin() + 1);

	return v;
}
*/
