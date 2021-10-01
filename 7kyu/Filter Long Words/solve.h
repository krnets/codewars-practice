#pragma once

#include <vector>
#include <string>
#include <algorithm>

#include <range/v3/all.hpp>
#include <range/v3/view/split.hpp>
#include <range/v3/to_container.hpp>
#include <range/v3/algorithm/remove_if.hpp>

/*
std::vector<std::string> filter_long_words(const std::string& sentence, int n)
{
	using namespace ranges;

	auto f = [n](auto word) { return word.size() <= n; };

	std::vector<std::string> vec = sentence
		| views::split(' ')
		| to<std::vector<std::string>>();

	vec.erase(std::ranges::remove_if(vec, f).begin(), vec.end());

	return vec;
}
*/

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
