#pragma once

#include <range/v3/algorithm/sort.hpp>
#include <range/v3/algorithm/transform.hpp>

/*
class Same
{
public :
	static bool comp(std::vector<int>& a, std::vector<int>& b)
	{
		if (a.size() != b.size()) return false;

		std::transform(a.begin(), a.end(), a.begin(), [](int x) { return x * x; });
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		return std::equal(a.begin(), a.end(), b.begin());
	}
};
*/

/*
class Same
{
public :
	static bool comp(std::vector<int>& a, std::vector<int>& b)
	{
		if (a.size() != b.size()) return false;

		ranges::transform(a, a.begin(), [](int x) { return x * x; });
		ranges::sort(a);
		ranges::sort(b);

		return std::equal(a.begin(), a.end(), b.begin());
	}
};
*/

class Same
{
public :
	static bool comp(std::vector<int>& a, std::vector<int>& b)
	{
		for_each(a.begin(), a.end(), [](int& x) { x *= x; });
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		return a == b;
	}
};

/*
class Same
{
public :
	static bool comp(std::vector<int>& a, std::vector<int>& b)
	{
		std::ranges::for_each(a, [](int& x) { x *= x; });
		std::ranges::sort(a);
		std::ranges::sort(b);

		return a == b;
	}
};
*/
