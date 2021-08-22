#include <vector>
#include <numeric>

/*
std::vector<int> reverseSeq(int n)
{
	std::vector<int> vec;

	for (int i = n; i > 0; --i)
	{
		vec.push_back(i);
	}

	return vec;
}
*/

/*
std::vector<int> reverseSeq(int n)
{
	std::vector<int> vec(n);

	std::iota(vec.begin(), vec.end(), 1);
	std::reverse(vec.begin(), vec.end());

	return vec;
}
*/

std::vector<int> reverseSeq(int n)
{
	std::vector<int> seq(n);

	std::iota(seq.rbegin(), seq.rend(), 1);

	return seq;
}
