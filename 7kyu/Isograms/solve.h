#pragma once
#include <set>

/*
bool is_isogram(std::string str)
{
	const int letters = 26;
	int arr[letters];
	std::fill(std::begin(arr), std::end(arr), 0);

	for (char c : str)
	{
		int i = ::tolower(c) - 'a';
		arr[i]++;
	}

	for (int i : arr)
		if (i > 1)
			return false;

	return true;
}
*/


bool is_isogram(std::string str)
{
	std::transform(str.begin(), str.end(), str.begin(), ::tolower);
	std::set<char> set(str.begin(), str.end());

	return set.size() == str.length();
}
