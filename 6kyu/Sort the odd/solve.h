#pragma once

#include <range/v3/view/filter.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/algorithm/sort.hpp>

using namespace ranges;
using std::vector;


/*
class Kata
{
public:
	vector<int> sortArray(vector<int> array)
	{
		vector<int> odd_pos, odd_nums;

		for (int i = 0; i < array.size(); ++i)
		{
			if (array[i] % 2 != 0)
			{
				odd_pos.push_back(i);
				odd_nums.push_back(array[i]);
			}
		}
		sort(odd_nums.begin(), odd_nums.end());

		for (int i = 0; i < odd_nums.size(); ++i)
		{
			array[odd_pos[i]] = odd_nums[i];
		}

		return array;
	}
};
*/

/*
class Kata
{
public:
	vector<int> sortArray(vector<int> array)
	{
		vector<int> odd_nums;
		auto is_odd = [](int x) { return x % 2 != 0; };
		std::copy_if(array.begin(), array.end(), std::back_inserter(odd_nums), is_odd);
		sort(odd_nums.begin(), odd_nums.end());

		for (int i = 0, pos = 0; i < array.size(); ++i)
			if (array[i] % 2 != 0)
				array[i] = odd_nums[pos++];

		return array;
	}
};
*/

class Kata
{
public:
	vector<int> sortArray(vector<int> array)
	{
		auto is_odd = [](int x) { return x % 2 != 0; };
		auto odd_nums = array | views::filter(is_odd) | to<vector<int>>();
		sort(odd_nums);
		int pos = 0;

		for (int& x : array)
			if (x % 2 != 0)
				x = odd_nums[pos++];

		return array;
	}
};
