/*
#include <vector>

int square_sum(const std::vector<int>& numbers)
{
	int ans = 0;
	
	for (int i = 0; i < numbers.size(); ++i)
	{
		ans += numbers.at(i) * numbers.at(i);
	}

	return ans;
}
*/

/*
#include <vector>

int square_sum(const std::vector<int>& numbers)
{
	int ans = 0;

	for (int num : numbers)
	{
		ans += (num * num);
	}

	return ans;
}
*/

/*
#include <numeric>
#include <vector>

int square_sum(const std::vector<int>& numbers)
{
	return std::accumulate(numbers.begin(), numbers.end(), 0, [](int a, int b) { return a + b * b; });
}
*/

#include <numeric>
#include <vector>

int square_sum(const std::vector<int>& numbers)
{
	return std::inner_product(numbers.begin(), numbers.end(), numbers.begin(), 0);
}
