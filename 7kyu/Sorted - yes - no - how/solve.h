#pragma once
#include <algorithm>

/*
std::string is_sorted_and_how(std::vector<int> array)
{
	bool b_ascending = false;
	bool b_descending = false;

	for (int i = 1; i < array.size(); ++i)
	{
		if (array[i - 1] < array[i])
			b_ascending = true;
		else if (array[i - 1] > array[i])
			b_descending = true;
	}

	return b_ascending && b_descending ? "no" : b_ascending ? "yes, ascending" : b_descending ? "yes, descending" : "";
}
*/

/*
std::string is_sorted_and_how(std::vector<int> array)
{
	bool b_ascending = std::is_sorted(array.begin(), array.end());
	bool b_descending = std::is_sorted(array.rbegin(), array.rend());

	return b_ascending ? "yes, ascending" : b_descending ? "yes, descending" : "no";
}
*/

/*
std::string is_sorted_and_how(std::vector<int> array)
{
	return std::is_sorted(array.begin(), array.end()) ? "yes, ascending" :
			 std::is_sorted(array.rbegin(), array.rend()) ? "yes, descending" : "no";
}
*/

std::string is_sorted_and_how(std::vector<int> array)
{
	bool b_ascending = std::adjacent_find(array.begin(), array.end(), std::greater<int>()) == array.end();
	bool b_descending = std::adjacent_find(array.begin(), array.end(), std::less<int>()) == array.end();

	return b_ascending ? "yes, ascending" : b_descending ? "yes, descending" : "no";
}
