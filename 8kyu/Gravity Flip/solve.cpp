#include <vector>
#include <algorithm>

std::vector<int> flip(const char dir, const std::vector<int>& arr)
{
	std::vector v(arr);

	if (dir == 'R')
		std::sort(v.begin(), v.end());
	if (dir == 'L')
		std::sort(v.rbegin(), v.rend());

	return v;
}
