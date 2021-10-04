#pragma once

#include <algorithm>

using std::vector;
using std::string;

/*
using namespace ranges;

vector<string> filter_long_words(const string& sentence, int n)
{
	vector<string> vec = views::split(sentence, ' ') | to<vector<string>>();

	auto pred = [n](string word) { return word.length() <= n; };

	vec.erase(remove_if(vec, pred), vec.end());

	return vec;
}
*/


/*vector<string> filter_long_words(const string& sentence, int n)
{
	std::istringstream iss(sentence);
	string word;
	vector<string> vec;

	while (std::getline(iss, word, ' '))
		if (word.length() > n)
			vec.push_back(word);

	return vec;
}*/

/*
vector<string> filter_long_words(const string& sentence, int n)
{
	std::istringstream iss(sentence);
	string word;
	vector<string> vec;

	while (iss >> word)
		if (word.length() > n)
			vec.push_back(word);

	return vec;
}
*/

#include <range/v3/view.hpp>

using namespace ranges;

vector<string> filter_long_words(const string& sentence, int n)
{
	vector<string> vec = sentence | views::split(' ') | to<vector<string>>();

	auto f = [n](auto word) { return word.size() > n; };

	return vec | views::filter(f) | ranges::to<vector<string>>();
}
