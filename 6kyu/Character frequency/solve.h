#pragma once

using list_t = std::vector<std::pair<char, size_t>>;

/*
list_t letter_frequency(const std::string& input)
{
	list_t result;
	int freq[128] = {};

	for (char c : input)
		if (c != ' ')
			freq[tolower(c)]++;

	for (char c = 'a'; c <= 'z'; ++c)
		if (freq[c])
			result.emplace_back(c, freq[c]);

	auto cmp = [](auto& x, auto& y)
	{
		if (x.second == y.second)
			return x.first < y.first;

		return x.second > y.second;
	};

	sort(result.begin(), result.end(), cmp);

	return result;
}
*/


list_t letter_frequency(const std::string& input)
{
	std::map<char, size_t> freq;

	for (char c : input)
		if (isalpha(c))
			freq[tolower(c)]++;

	list_t result(freq.begin(), freq.end());

	auto pred = [](auto& x, auto& y)
	{
		if (x.second == y.second)
			return x.first < y.first;

		return x.second > y.second;
	};

	sort(result.begin(), result.end(), pred);

	return result;
}
