#pragma once

#include <numeric>
#include <vector>

using namespace std;

/*
vector<int> arrayLeaders(const vector<int>& numbers)
{
	vector<int> v;

	for (auto it = numbers.begin(); it != numbers.end(); ++it)
		if (*it > accumulate(it + 1, numbers.end(), 0))
			v.push_back(*it);

	return v;
}
*/

/*
vector<int> arrayLeaders(const vector<int>& numbers)
{
	vector<int> v;
	int sum = 0;

	for (auto it = numbers.rbegin(); it != numbers.rend(); ++it)
	{
		if (*it > sum)
		{
			v.push_back(*it);
		}
		sum += *it;
	}

	ranges::reverse(v);

	return v;
}*/


vector<int> arrayLeaders(const vector<int>& numbers)
{
	vector<int> v;
	int sum = 0;

	for_each(numbers.rbegin(), numbers.rend(), [&](int x)
	{
		if (x > sum) v.push_back(x);
		sum += x;
	});

	reverse(v.begin(), v.end());

	return v;
}
