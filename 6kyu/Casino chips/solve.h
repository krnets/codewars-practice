#pragma once

#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/algorithm/max_element.hpp>

using namespace ranges;
using std::vector;

int solve(vector<int> v)
{
	int sum = accumulate(v, 0);
	int mx = *max_element(v);

	return std::min(sum / 2, sum - mx);
}
