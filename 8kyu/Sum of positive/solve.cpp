#include <vector>

int positive_sum(const std::vector<int> arr)
{
	int sum = 0;

	for (const int x : arr)
		if (x > 0)
			sum += x;

	return sum;
}
