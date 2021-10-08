#pragma once

#include <range/v3/algorithm/min_element.hpp>
#include <range/v3/algorithm/max_element.hpp>
#include <range/v3/algorithm/find.hpp>

using namespace ranges;
using std::vector;

/*
long queueTime(vector<int> customers, int n)
{
	vector<int> tills(n);

	for (int customer : customers)
	{
		int shortest = *min_element(tills);
		int i = find(tills, shortest) - tills.begin();

		tills[i] = shortest + customer;
	}
	return *max_element(tills);
}
*/

/*
long queueTime(vector<int> customers, int n)
{
	vector<int> tills(n);

	for (int& customer : customers)
	{
		*std::min_element(tills.begin(), tills.end()) += customer;
	}
	return *std::max_element(tills.begin(), tills.end());
}
*/

long queueTime(vector<int> customers, int n)
{
	vector<int> tills(n);

	for (int& customer : customers)
	{
		*min_element(tills) += customer;
	}
	return *max_element(tills);
}
