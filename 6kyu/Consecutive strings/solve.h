#pragma once

#include <numeric>

#include <range/v3/view/sliding.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/view/join.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/algorithm/max_element.hpp>

using namespace ranges;
using std::string;
using std::vector;

/*
class LongestConsec
{
public:
	static string longestConsec(vector<string>& strarr, int k)
	{
		if (k <= 0) return string();

		auto rng = strarr
			| views::sliding(k)
			| views::transform([](auto vec) { return vec | views::join | to<string>(); })
			| to<vector<string>>();

		string longest;

		for (auto current : rng)
			if (current.length() > longest.length())
				longest = current;

		return longest;
	}
};
*/

class LongestConsec
{
public:
	static string longestConsec(vector<string>& strarr, int k)
	{
		if (k <= 0 || k > strarr.size()) return string();

		auto rng = strarr
			| views::sliding(k)
			| views::transform([](auto vec) { return vec | views::join | to<string>(); });

		return *max_element(rng, [](string a, string b) { return a.length() < b.length(); });
	}
};

/*
class LongestConsec
{
public:
	static string longestConsec(vector<string>& strarr, int k)
	{
		int longest = 0, pos = 0, end = strarr.size();

		if (k <= 0 || k > end) return string();

		for (int i = 0; i < k; ++i)
		{
			longest += strarr[i].length();
		}
		int sum = longest;

		for (int i = k; i < end; ++i)
		{
			sum += strarr[i].length();
			sum -= strarr[i - k].length();

			if (sum > longest)
			{
				longest = sum;
				pos = i - k + 1;
			}
		}
		return accumulate(strarr.begin() + pos, strarr.begin() + pos + k, string());
	}
};
*/
