#pragma once

/*
std::vector<int> bubbleSortOnce(const std::vector<int>& input)
{
	std::vector vec(input);

	for (size_t i = 1; i < vec.size(); ++i)
		if (vec[i - 1] > vec[i])
			std::swap(vec[i - 1], vec[i]);

	return vec;
}
*/

using std::vector;

vector<int> bubbleSortOnce(const vector<int>& input)
{
	vector v(input);

	auto f = [](auto& lhs, auto& rhs)
	{
		if (lhs > rhs)
			std::swap(lhs, rhs);

		return lhs;
	};

	std::transform(v.begin(), prev(v.end()), next(v.begin()),
	               v.begin(), f);
	return v;
}
