#pragma once

#include <range/v3/numeric/accumulate.hpp>

/*
static long findMissing(std::vector<long> list)
{
	long expected_sum = (list.front() + list.back()) * (static_cast<long double>(list.size() + 1) / 2);

	long actual_sum = ranges::accumulate(list, 0L);

	return expected_sum - actual_sum;
}
*/

static long findMissing(std::vector<long> list)
{
	long expected_sum = (list.front() + list.back()) * ((list.size() + 1) / 2.0);

	long actual_sum = ranges::accumulate(list, 0L);

	return expected_sum - actual_sum;
}

/*
#include <numeric>

static long findMissing(std::vector<long> list)
{
	long double expectedSum = (((long double)list.size() + 1) / 2) * (list.back() + list.front());
	long actualSum = std::accumulate(list.begin(), list.end(), (long)0);

	return expectedSum - actualSum;
}*/

/*
static long findMissing(std::vector<long> list)
{
	long step = (list.back() - list.front()) / static_cast<long>(list.size());

	for (int i = 1; i < list.size(); ++i)
		if (list[i] - list[i - 1] != step)
			return list[i - 1] + step;

	return -1;
}
*/
