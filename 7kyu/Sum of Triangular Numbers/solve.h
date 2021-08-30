#pragma once
#include <numeric>

/*
int sumTriangularNumbers(int n)
{
	if (n < 1)
		return 0;

	std::vector<int> v;
	v.reserve(n);
	v.push_back(1);

	for (int i = 1; i < n; ++i)
	{
		v.push_back(v.at(i - 1) + (i + 1));
	}

	return std::accumulate(v.begin(), v.end(), 0);
}
*/

/*
int sumTriangularNumbers(int n)
{
	if (n < 1) return 0;

	int sum = 1, curr, prev = 1;

	for (int i = 2; i <= n; ++i)
	{
		curr = prev + i;
		sum += curr;
		prev = curr;
	}

	return sum;
}
*/

/*
int sumTriangularNumbers(int n)
{
	int sum = 0;

	for (int i = 1; i <= n; ++i)
	{
		sum += (i * (i + 1) / 2);
	}

	return sum;
}
*/

int sumTriangularNumbers(int n)
{
	return (n > 0) * (n + 1) * (n + 2) * n / 6;
}
