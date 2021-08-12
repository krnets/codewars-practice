#include <vector>
#include <numeric>

/*
std::vector<int> MonkeyCount(int n)
{
	std::vector<int> v(n);

	for (int i = 1; i <= n; ++i)
	{
		v[i - 1] = i;
	}

	return v;
}
*/

std::vector<int> MonkeyCount(int n)
{
	std::vector<int> v(n);

	std::iota(v.begin(), v.end(), 1);

	return v;
}
