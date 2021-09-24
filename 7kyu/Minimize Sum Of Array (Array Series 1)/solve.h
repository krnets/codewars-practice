#pragma once
#include <numeric>
#include <vector>

// using namespace std;

/*
int minSum(vector<int> passed)
{
	sort(passed.begin(), passed.end());

	int ans = 0;
	int length = passed.size();
	int mid = length / 2;

	for (int i = 0; i < mid; ++i)
	{
		ans += (passed[i] * passed[length - i - 1]);
	}

	return ans;
}
*/

int minSum(std::vector<int> passed)
{
	std::sort(passed.begin(), passed.end());
	int mid = passed.size() / 2;

	return std::inner_product(passed.begin(), passed.begin() + mid, passed.rbegin(), 0);
}
