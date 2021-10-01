#pragma once

#include <deque>
#include <vector>

/*
std::vector<int> Pendulum(std::vector<int> values)
{
	sort(values.begin(), values.end());
	int n = values.size();
	int pos = (n - 1) / 2;
	std::vector<int> result(n);

	for (int i = 0; i < n; ++i)
	{
		pos += (i % 2 ? i : -i);

		result[pos] = values[i];
	}

	return result;
}
*/


/*
std::vector<int> Pendulum(std::vector<int> values)
{
	sort(values.begin(), values.end());
	int n = values.size();
	int pos = n - 1 >> 1;
	std::vector<int> result(n);

	for (int i = 0; i < n; ++i)
	{
		pos += (i & 1 ? i : -i);

		result[pos] = values[i];
	}

	return result;
}
*/

std::vector<int> Pendulum(std::vector<int> values)
{
	std::sort(values.begin(), values.end());
	std::deque<int> deq;

	for (int i = 0; i < values.size(); ++i)
		if (i & 1)
			deq.push_back(values[i]);
		else
			deq.push_front(values[i]);

	return std::vector(deq.begin(), deq.end());
}
