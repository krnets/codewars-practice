#pragma once

#include <range/v3/algorithm/copy.hpp>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/take.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::vector;

/*
vector<int> xbonacci(vector<int> signature, int n)
{
	if (n < signature.size())
		return signature | views::take(n) | to<vector<int>>();

	vector<int> v(n);
	copy(signature, v.begin());
	int len = signature.size();
	int pos = len;

	while (pos < n)
		v[pos++] = accumulate(v.begin() + pos - len, v.begin() + pos, 0);

	return v;
}
*/

/*
std::vector<int> xbonacci(std::vector<int> signature, int n)
{
	if (n <= signature.size())
	{
		signature.resize(n);
	}
	else
	{
		signature.push_back(ranges::accumulate(signature, 0));

		const size_t x = signature.size();

		for (int i = x; i < n; ++i)
		{
			int sum = 2 * signature[i - 1] - signature[i - x];

			signature.push_back(sum);
		}
	}
	return signature;
}
*/

/*
std::vector<int> xbonacci(std::vector<int> signature, int n)
{
	if (n <= signature.size())
		signature.resize(n);
	else
	{
		signature.push_back(ranges::accumulate(signature, 0));
		int size = signature.size();

		for (int i = size; i < n; ++i)
		{
			int sum = 2 * signature[i - 1] - signature[i - size];
			signature.push_back(sum);
		}
	}
	return signature;
}
*/

std::vector<int> xbonacci(std::vector<int> signature, int n)
{
	signature.reserve(n);
	signature.push_back(accumulate(signature, 0));
	int x = signature.size();

	for (int i = x; i < n; ++i)
		signature.push_back(2 * signature[i - 1] - signature[i - x]);

	signature.resize(n);

	return signature;
}
