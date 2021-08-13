#include <vector>
#include <numeric>


/*
int grow(std::vector<int> nums)
{
	return std::accumulate(nums.begin(), nums.end(), 1, [](int a, int b) { return a * b; });
}
*/


int grow(std::vector<int> nums)
{
	return std::accumulate(nums.cbegin(), nums.cend(), 1, std::multiplies<int>());
}
