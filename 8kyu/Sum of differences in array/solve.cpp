#include <vector>
#include <algorithm>

/*
int sumOfDifferences(const std::vector<int>& arr)
{
	std::vector<int> v(arr);
	std::sort(v.rbegin(), v.rend());
	int sum = 0;

	for (int i = 1; i < v.size(); ++i)
	{
		sum += v.at(i) - v.at(i - 1);
	}

	return abs(sum);
}
*/

int sumOfDifferences(const std::vector<int>& arr)
{
	if (arr.empty()) return 0;

	auto pair = std::minmax_element(arr.begin(), arr.end());

	return *pair.second - *pair.first;
}
