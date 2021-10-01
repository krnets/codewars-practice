#pragma once
#include <deque>

class Valley
{
public:
	static std::vector<int> makeValley(std::vector<int>& arr)
	{
		std::deque<int> left, right;
		std::vector v(arr);
		std::sort(v.begin(), v.end(), std::greater());

		for (int i = 0; i < v.size(); ++i)
		{
			if (i % 2 == 0)
				left.push_back(v[i]);
			else
				right.push_front(v[i]);
		}
		std::copy(left.begin(), left.end(), v.begin());
		std::copy(right.begin(), right.end(), v.begin() + left.size());

		return v;
	}
};
