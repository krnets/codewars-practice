#include <vector>
#include <algorithm>

/*
std::vector<int> countBy(int x, int n)
{
	std::vector<int> result(n);

	for (int i = 1; i <= n; ++i)
	{
		result[i - 1] = x * i;
	}

	return result;
}
*/

/*
std::vector<int> countBy(int x, int n)
{
	std::vector<int> v(n);
	std::generate(v.begin(), v.end(), [x, y = 0]() mutable { return y += x; });

	return v;
}
*/

std::vector<int> countBy(int x, int n)
{
	std::vector<int> v(n);
	std::generate_n(v.rbegin(), n, [&]() { return x * n--; });

	return v;
}
