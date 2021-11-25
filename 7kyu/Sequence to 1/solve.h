#pragma once
#include <range/v3/numeric/iota.hpp>
#include <range/v3/algorithm/reverse.hpp>

using namespace ranges;
using std::vector;

/*
vector<int> seqToOne(int n)
{
	vector<int> v;

	if (n < 1)
	{
		while (n <= 1)
		{
			v.push_back(n);
			++n;
		}
	}
	else
	{
		while (n > 0)
		{
			v.push_back(n);
			--n;
		}
	}

	return v;
}
*/

vector<int> seqToOne(int n)
{
	vector<int> v(n < 0 ? 2 - n : n);

	if (n < 0)
		iota(v, n);
	else
	{
		iota(v, 1);
		reverse(v);
	}

	return v;
}
