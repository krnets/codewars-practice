#pragma once
#include <list>
#include <range/v3/numeric/accumulate.hpp>

/*
int findDeletedNumber(std::list<int> startingList, std::list<int> mixedList)
{
	int x = ranges::accumulate(startingList, 0);
	int y = ranges::accumulate(mixedList, 0);

	return abs(x - y);
}
*/

using namespace std;

int findDeletedNumber(list<int> startingList, list<int> mixedList)
{
	set a(startingList.begin(), startingList.end());
	set b(mixedList.begin(), mixedList.end());
	vector<int> v;
	set_difference(a.begin(), a.end(), b.begin(), b.end(), back_inserter(v));

	return v.empty() ? 0 : v.front();
}
