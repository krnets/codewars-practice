#pragma once
#include <numeric>

/*
char add_letters(std::vector<char> letters)
{
	if (letters.empty())
		return 'z';

	int sum = 0;

	for (char c : letters)
	{
		sum += (c - 'a' + 1);
	}

	return (sum - 1) % 26 + 'a';
}
*/


char add_letters(std::vector<char> letters)
{
	int sum = std::accumulate(letters.begin(), letters.end(), 0,
	                          [](int x, char c) { return x + (c - 'a' + 1); });

	return letters.empty() ? 'z' : (sum - 1) % 26 + 'a';
}
