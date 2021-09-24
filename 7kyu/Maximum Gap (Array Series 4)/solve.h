#pragma once

#include <vector>
#include <numeric>

using namespace std;

int maxGap(vector<int> numbers)
{
	ranges::sort(numbers);
	std::adjacent_difference(numbers.begin(), numbers.end(), numbers.begin());

	return *ranges::max_element(numbers);
}
