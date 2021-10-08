#pragma once

// #include <range/v3/all.hpp>
#include <range/v3/action/split.hpp>
#include <range/v3/numeric/accumulate.hpp>
#include <range/v3/view/transform.hpp>
#include <range/v3/view/zip.hpp>
#include <range/v3/algorithm/max_element.hpp>

using namespace ranges;
using std::string;

/*
string highestScoringWord(const string& str)
{
	auto words = actions::split(str, ' ');

	auto get_char_value = [](char c) { return c - 'a' + 1; };

	auto get_score = [&](string word) { return accumulate(word | views::transform(get_char_value), 0); };

	auto scores = words | views::transform(get_score);

	auto zipped = views::zip(words, scores);

	auto cmp = [](auto x, auto y) { return x.second < y.second; };

	auto ans = *max_element(zipped, cmp);

	return ans.first;
}
*/

/*
string highestScoringWord(const string& str)
{
	std::vector<string> words;
	std::istringstream iss(str);
	string word;

	while (iss >> word) words.push_back(word);

	auto get_char_value = [](char c) { return c - 'a' + 1; };

	auto get_score = [&](string word) { return accumulate(word | views::transform(get_char_value), 0); };

	auto scores = words | views::transform(get_score);

	auto zipped = views::zip(words, scores);

	auto cmp = [&](auto x, auto y) { return x.second < y.second; };

	auto ans = *max_element(zipped, cmp);

	return ans.first;
}
*/

string highestScoringWord(const string& str)
{
	string ans, word;
	std::istringstream iss(str);
	int max = 0;

	while (iss >> word)
	{
		int score = 0;

		for (char c : word)
			score += c - 'a' + 1;

		if (score > max)
		{
			max = score;
			ans = word;
		}
	}

	return ans;
}
