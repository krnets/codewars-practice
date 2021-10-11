#pragma once

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/algorithm/reverse.hpp>

using namespace ranges;
using std::string;

class PlayPass
{
public:
	static string playPass(const string& s, int n)
	{
		auto shift_n = [n](char c)
		{
			char res = c;
			if (isdigit(c))
				res = abs(c - '0' - 9) + '0';
			else if (isalpha(c))
				res = (c - 'A' + n) % 26 + 'A';
			return res;
		};

		string ans = s | views::transform(shift_n) | to<string>();

		for (int i = 0; i < ans.length(); ++i)
			if (i & 1)
				ans[i] = tolower(ans[i]);

		reverse(ans);

		return ans;
	}
};
