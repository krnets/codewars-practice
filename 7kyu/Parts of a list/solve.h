#pragma once
#include <numeric>

using std::vector;
using std::pair;
using std::string;

/*class PartList
{
public:
	static vector<pair<string, string>> partlist(vector<string>& arr)
	{
		vector<pair<string, string>> ans;

		for (int i = 1; i < arr.size(); ++i)
		{
			string first, second;

			for (int j = 0; j < i; ++j)			 first.append(arr[j]).append(" ");
			for (int j = i; j < arr.size(); ++j) second.append(arr[j]).append(" ");

			first.pop_back();
			second.pop_back();

			pair<string, string> p = std::make_pair(first, second);

			ans.push_back(p);
		}

		return ans;
	}
};*/

/*
class PartList
{
public:
	static vector<pair<string, string>> partlist(vector<string>& arr)
	{
		vector<pair<string, string>> ans;

		for (int i = 1; i < arr.size(); ++i)
		{
			string first, second;

			for (int j = 0; j < i; ++j)           first.append(arr[j]).append(" ");
			for (int j = i; j < arr.size(); ++j) second.append(arr[j]).append(" ");

			first.pop_back();
			second.pop_back();
			ans.emplace_back(first, second);
		}

		return ans;
	}
};
*/

class PartList
{
public:
	static vector<pair<string, string>> partlist(vector<string>& arr)
	{
		vector<pair<string, string>> ans;
		auto join = [](string a, string b) { return a.append(" ").append(b); };

		for (int i = 1; i < arr.size(); ++i)
		{
			string first = std::accumulate(arr.begin() + 1, arr.begin() + i, arr[0], join);
			string second = std::accumulate(arr.begin() + i + 1, arr.end(), arr[i], join);

			ans.emplace_back(first, second);
		}

		return ans;
	}
};
