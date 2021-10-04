#pragma once
// #include <range/v3/all.hpp>

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using std::string;
using std::vector;

string to_lowercase(string word)
{
	return word | ranges::views::transform(tolower) | ranges::to<string>();
};

/*
string well(const vector<vector<string>>& arr)
{
	int count_good = 0;

	for (int i = 0; i < arr.size(); ++i)
		for (int j = 0; j < arr[i].size(); ++j)
			if (to_lowercase(arr[i][j]) == "good")
				count_good++;

	return count_good > 2 ? "I smell a series!" : count_good > 0 ? "Publish!" : "Fail!";
}
*/

string well(const vector<vector<string>>& arr)
{
	int count_good = 0;

	for (const auto& vec : arr)
		for (const auto& word : vec)
			if (to_lowercase(word) == "good")
				count_good++;

	return count_good > 2 ? "I smell a series!" : count_good > 0 ? "Publish!" : "Fail!";
}
