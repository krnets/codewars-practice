#include <vector>
#include <numeric>

std::vector<int> arr(int n = 0)
{
	std::vector<int> vec(n);
	std::iota(vec.begin(), vec.end(), 0);

	return vec;
}
