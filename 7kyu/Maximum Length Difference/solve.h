#pragma once

class MaxDiffLength
{
public:
	static int mxdiflg(std::vector<std::string>& a1, std::vector<std::string>& a2)
	{
		if (a1.empty() || a2.empty()) return -1;

		auto cmp = [](auto s1, auto s2) { return s1.size() < s2.size(); };

		auto a1pair = std::minmax_element(a1.begin(), a1.end(), cmp);
		auto a2pair = std::minmax_element(a2.begin(), a2.end(), cmp);

		int a1min = a1pair.first->size();
		int a1max = a1pair.second->size();

		int a2min = a2pair.first->size();
		int a2max = a2pair.second->size();

		return std::max(abs(a1min - a2max), abs(a2min - a1max));
	}
};

/*
class MaxDiffLength
{
public:
	static int mxdiflg(std::vector<std::string>& a1, std::vector<std::string>& a2)
	{
		int maxDiff = -1;

		for (auto s1 : a1)
		{
			int x = s1.size();

			for (auto s2 : a2)
			{
				int y = s2.size();

				maxDiff = std::max(abs(x - y), maxDiff);
			}
		}

		return maxDiff;
	}
};
*/
