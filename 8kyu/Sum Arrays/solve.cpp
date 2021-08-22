#include <vector>
#include <numeric>

/*int sum(std::vector<int> nums)
{
	int ans = 0;

	for (int num : nums)
		ans += num;

	return ans;
}*/

int sum(std::vector<int> nums)
{
	return std::accumulate(nums.begin(), nums.end(), 0);
}
