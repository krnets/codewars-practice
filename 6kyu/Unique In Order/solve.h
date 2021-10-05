#pragma once

using std::string;
using std::vector;

/*
#include <range/v3/view/unique.hpp>
#include <range/v3/to_container.hpp>

using namespace ranges;

template <typename T>
vector<T> uniqueInOrder(const vector<T>& iterable)
{
	return iterable | views::unique | to<vector<T>>();
}

vector<char> uniqueInOrder(const string& iterable)
{
	return iterable | views::unique | to<vector<char>>();
}
*/


template <typename T>
vector<T> uniqueInOrder(const vector<T>& iterable)
{
	if (iterable.empty()) return iterable;

	vector<T> v;
	v.reserve(iterable.size());
	T last = iterable.front();
	v.push_back(last);

	for (auto it = iterable.begin() + 1; it != iterable.end(); ++it)
	{
		if (*it != last)
			v.push_back(*it);

		last = *it;
	}

	return v;
}

vector<char> uniqueInOrder(const string& iterable)
{
	vector<char> v(iterable.begin(), iterable.end());

	return uniqueInOrder(v);
}
