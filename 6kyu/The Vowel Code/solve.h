#pragma once

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;

/*
string encode(const string& str)
{
	std::map<char, char> md{{'a', '1'}, {'e', '2'}, {'i', '3'}, {'o', '4'}, {'u', '5'}};

	auto to_digit = [&](char c) { return md.find(c) == md.end() ? c : md[c]; };

	return str | views::transform(to_digit) | to<string>();
}

string decode(const string& str)
{
	std::map<char, char> ml{{'1', 'a'}, {'2', 'e'}, {'3', 'i'}, {'4', 'o'}, {'5', 'u'}};

	auto to_vowel = [&](char c) { return ml.find(c) == ml.end() ? c : ml[c]; };

	return str | views::transform(to_vowel) | to<string>();
}
*/

const string vowels = "aeiou";

/*
string encode(const string& str)
{
	string res(str);

	for (char& c : res)
	{
		int pos = vowels.find(c);

		if (pos != -1)
			c = pos + '1';
	}

	return res;
}
*/

/*
string decode(const string& str)
{
	string res(str);

	for (char& c : res)
		if (c > '0' && c <= '5')
			c = vowels[c - '1'];

	return res;
}
*/

string encode(const string& str)
{
	auto to_digit = [](char c)
	{
		int idx = vowels.find(c);
		return idx == -1 ? c : idx + '1';
	};

	return str | views::transform(to_digit) | to<string>();
}

string decode(const string& str)
{
	auto to_vowel = [](char c) { return c > '0' && c <= '5' ? vowels[c - '1'] : c; };

	return str | views::transform(to_vowel) | to<string>();
}
