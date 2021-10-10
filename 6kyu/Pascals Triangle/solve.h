#pragma once

// #include <range/v3/all.hpp>

#include <range/v3/view/join.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::vector;

/*
vector<long long> pascalsTriangle(int n)
{
	vector<vector<long long>> triangle;

	for (int i = 0; i < n; ++i)
	{
		vector<long long> row(i + 1);
		row[0] = 1;
		row[i] = 1;

		for (int j = 1; j < i; ++j)
		{
			row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
		}
		triangle.push_back(row);
	}
	return triangle | views::join | to<vector<long long>>();
}
*/

vector<long long> pascalsTriangle(int n)
{
	vector<long long> result;

	for (int i = 0; i < n; ++i)
	{
		long long num = 1;

		for (int j = 0; j <= i; ++j)
		{
			result.push_back(num);

			num = num * (i - j) / (j + 1);
		}
	}
	return result;
}
