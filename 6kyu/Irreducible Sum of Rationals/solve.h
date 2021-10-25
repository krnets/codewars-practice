#pragma once

#include <numeric>
#include <utility>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/transform.hpp>

using namespace ranges;
using std::vector;

/*
class SumFractions
{
public:
	static std::pair<int, int> sumFracts(vector<vector<int>>& l)
	{
		int denom = accumulate(l, 1, [](int acc, auto& vec) { return acc * vec[1]; });

		auto rng = l | views::transform([&](auto& vec) { return vec[0] * denom / vec[1]; });
		int numer = accumulate(rng, 0);

		int gcd_val = std::gcd(numer, denom);

		return std::make_pair(numer / gcd_val, denom / gcd_val);
	}
};
*/

class SumFractions
{
public:
	static std::pair<int, int> sumFracts(std::vector<std::vector<int>>& l)
	{
		int numer = 0, denom = 1;

		for (auto& vec : l) { denom *= vec[1]; }
		for (auto& vec : l) { numer += vec[0] * denom / vec[1]; }

		int gcd_val = std::gcd(numer, denom);

		return {numer / gcd_val, denom / gcd_val};
	}
};
