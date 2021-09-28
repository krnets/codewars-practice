#pragma once
#include <queue>

/*
#include <range/v3/algorithm/sort.hpp>

int minimumSteps(std::vector<int> numbers, int input)
{
	int steps = 0, sum = 0;
	ranges::sort(numbers);

	for (int number : numbers)
	{
		sum += number;

		if (sum >= input)
			break;

		steps++;
	}

	return steps;
}
*/

int minimumSteps(std::vector<int> numbers, int input)
{
	std::priority_queue<int, std::vector<int>, std::greater<>> pq({}, numbers);
	int steps = 0, sum = 0;

	while (sum < input)
	{
		sum += pq.top();
		pq.pop();
		steps++;
	}

	return steps - 1;
}
