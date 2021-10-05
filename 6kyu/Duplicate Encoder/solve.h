#pragma once

#include <range/v3/view/transform.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;
using std::string;

string duplicate_encoder(const string& word)
{
	auto lowercase = word | views::transform(tolower) | to<string>();

	std::map<char, int> freq;

	for (char c : lowercase) freq[c]++;

	return lowercase | views::transform([&](char c) { return freq[c] == 1 ? '(' : ')'; }) | to<string>();
}
