#include <vector>
#include <algorithm>

/*int min(std::vector<int> list)
{
	int ans = INT32_MAX;

	for (int x : list)
		if (x < ans)
			ans = x;

	return ans;
}

int max(std::vector<int> list)
{
	int ans = INT32_MIN;

	for (int x : list)
		if (x > ans)
			ans = x;

	return ans;
}*/

int min(std::vector<int> list) { return *std::min_element(list.begin(), list.end()); }

int max(std::vector<int> list) { return *std::max_element(list.begin(), list.end()); }
