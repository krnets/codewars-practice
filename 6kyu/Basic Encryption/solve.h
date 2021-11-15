#pragma once
#include <range/v3/all.hpp>

using namespace ranges;
using std::string;

/*
string encrypt(string text, int rule)
{
	transform(text, text.begin(), [rule](char c)
	{
		return (c + rule) % 256;
	});

	return text;
};
*/

string encrypt(string text, int rule)
{
	for (char& c : text)
	{
		c = (c + rule) % 256;
	}
	return text;
};
