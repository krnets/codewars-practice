#include <vector>
#include <numeric>

int arrayPlusArray(std::vector<int> a, std::vector<int> b)
{
	int sum_a = std::accumulate(a.begin(), a.end(), 0);
	int sum_b = std::accumulate(b.begin(), b.end(), 0);

	return sum_a + sum_b;
}
