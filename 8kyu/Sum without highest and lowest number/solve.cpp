#include <vector>
#include <algorithm>
#include <numeric>

/*
int sum(std::vector<int> numbers)
{
	if (numbers.size() < 2) return 0;

	int min = *std::min_element(numbers.begin(), numbers.end());
	int max = *std::max_element(numbers.begin(), numbers.end());
	int sum = std::accumulate(numbers.begin(), numbers.end(), 0);

	return sum - min - max;
}
*/

/*
int sum(std::vector<int> numbers)
{
	std::sort(numbers.begin(), numbers.end());

	int ans = 0;
	int n = numbers.size() - 1;

	for (int i = 1; i < n; ++i)
	{
		ans += numbers[i];
	}

	return ans;
}
*/

int sum(std::vector<int> numbers)
{
	int ans = 0;

	if (numbers.size() < 2) return ans;

	int min = INT32_MAX;
	int max = INT32_MIN;

	for (int number : numbers)
	{
		if (number < min) min = number;
		if (number > max) max = number;

		ans += number;
	}

	return ans - min - max;
}
